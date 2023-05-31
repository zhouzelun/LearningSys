from flask import Blueprint,render_template,g,request,jsonify,session,redirect,flash
from permission import Permissions,permission_required
from forms import LoginForm
import database

bp = Blueprint("login",__name__,url_prefix="/login")
@bp.route('/',methods=['GET','POST'])
def login():
    
    if request.method=='GET':
        userid = session.get('nl_user_id') 
        login_user = database.get_user_byid(userid)
        if login_user is not None:
            return redirect("../")
        else:
            return render_template("login.html",message='')
    elif request.method=='POST' and 'username' in request.form.keys():
        form = LoginForm(request.form)
        loginname=form.username.data
        loginpassword=form.password.data
        login_user = database.get_user_byloginname(loginname)
        if login_user is None:
            message = '该用户不存在'
            return render_template("login.html",message=message)
        elif login_user[0].password != loginpassword:
            message = '账号密码不匹配'
            return render_template("login.html",message=message)
        else:
            session['nl_user_id'] = login_user[0].userid
            return redirect(request.referrer or "/")