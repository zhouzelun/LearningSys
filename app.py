from flask import Flask, jsonify,render_template, request,session,redirect,url_for,flash,g,send_file
import config
import database
from blueprints import login_bp, mobile_information_bp, paper_bp,users_bp,information_bp,manage_bp
from sqlalchemy import select
from permission import Permissions,permission_required
import os
import json
import logging
import datetime

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(paper_bp)
app.register_blueprint(users_bp)
app.register_blueprint(login_bp)
app.register_blueprint(information_bp)
app.register_blueprint(mobile_information_bp)
app.register_blueprint(manage_bp)

engine = database.engine
#logging.basicConfig(filename=datetime.datetime.now().strftime("%Y-%m-%d")+'.log',level=logging.DEBUG)
@app.before_request
def before_function():
    userid = session.get('nl_user_id') 
    login_user = database.get_user_byid(userid)
    if login_user is not None:
        setattr(g,'user',login_user[0])
        if login_user[0].roleid == 0:
            setattr(g,'ismanage',1)
        else :
            setattr(g,'ismanage',None)
    else:
        setattr(g,'user',None)

@app.context_processor
def context_function():
    useragnet = request.headers.get ("User-Agent") 
    data = {}
    data["frommobile"] = 0
    mobilestring ='mobile|android|iphone|ipod|phone|ipad'
    for str in mobilestring.split('|'):
        if(str in useragnet.lower()):
            data["frommobile"] = 1
    if hasattr(g,'user'):
        data["user"] = g.user
    if hasattr(g,'ismanage'):
        data["manage"] = g.ismanage
    return data

@app.route('/loginout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='GET':
        return render_template("index.html")
    '''elif  request.method=='POST' and 'username' in request.form.keys():
        form = LoginForm(request.form)
        loginname=form.username.data
        loginpassword=form.password.data
        login_user = database.get_user_byloginname(loginname)
        if login_user is None:
            return jsonify("该账户不存在")
        elif login_user[0].password != loginpassword:
            return jsonify("账号密码不匹配")
        else:
            session['nl_user_id'] = login_user[0].userid
            return jsonify("refresh") '''

@app.route('/<path:url_path>/<file_name>', methods=['GET']) #泛型
def get_file(url_path,file_name):
    file_path = os.path.join(url_path, file_name)
    return send_file(file_path)

# @app.route('/media/<file_name>', methods=['GET']) #泛型
# def get_media(file_name):
#     file_name = file_name.replace('%', '/')
#     file_path = os.path.join('media', file_name)
#     return send_file(file_path)


@app.route('/createcenter',methods=['GET'])
@permission_required(Permissions.ANONYMOUS_PERMISSION)
def show_createcenter():
     return render_template('createcenter.html')

@app.route('/postguidbarjson',methods=['post','get'])
def postguidbarjson():

    index = request.form.get ("index") 
    with open("guidbar.json",'w') as load_f:
        load_dict={ "img1":1, "img2":0,"img3":0}
        match index:
            case '1':load_dict={ "img1":1, "img2":0,"img3":0}
            case '2':load_dict={ "img1":0, "img2":1,"img3":0}
            case '3':load_dict={ "img1":0, "img2":0,"img3":1}
        json.dump(load_dict,load_f)
    return render_template('createcenter.html')
    
@app.route('/getguidbarjson',methods=['post','get'])
def getguidbarjson():
    with open("guidbar.json",'r') as load_f:
        content = load_f.read()
        data = json.loads(content)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=80)