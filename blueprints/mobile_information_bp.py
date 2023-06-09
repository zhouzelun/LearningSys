from flask import Blueprint, render_template,request,redirect,flash
from permission import Permissions,permission_required
from flask import current_app,jsonify,session,g
from database import insert_article,get_all_article,get_article_byid,\
delete_article,insert_readrecord,get_user_readrecord,get_all_article_filterbystate,get_alluser,get_alldepartment
import shutil
import os
from selectolax.parser import HTMLParser
import pypinyin
a = pypinyin.pinyin ( '姓名', style=pypinyin.FIRST_LETTER)
bp = Blueprint("mobile_information",__name__,url_prefix="/mobile_information")

@bp.route('/createarticle',methods=['GET'])
@permission_required(Permissions.ANONYMOUS_PERMISSION)
def createarticle():
    users = get_alluser()
    userlist = []
    for item in users:
        namepylist = pypinyin.pinyin ( item.username, style=pypinyin.FIRST_LETTER)
        namepy = ''.join(i[0] for i in namepylist)
        userlist.append({'userid':item.userid,'name':item.username,'py':namepy})

    departments = get_alldepartment()
    departmentlist = []
    for item in departments:
        departnamelist = pypinyin.pinyin ( item.departmentname, style=pypinyin.FIRST_LETTER)
        departpy = ''.join(i[0] for i in departnamelist)
        departmentlist.append({'departmentid':item.departmentid,'name':item.departmentname,'py':departpy})
    return render_template('publishinform.html',userlist=userlist,departmentlist= departmentlist)

@bp.route('/richarea',methods=['GET','POST'])
@permission_required(Permissions.ANONYMOUS_PERMISSION)
def show_richarea():
     return render_template('richarea.html')


@bp.route('/uploadimage',methods=['GET','POST'])
def uploadimage():
     imageFolder = 'images/'
     myimage = request.files.get("file")
     fname= myimage.filename
     fp=os.path.join(imageFolder,fname)
     myimage.save(fp)
     data={
          "location": '../images/'+fname
     }  
     return jsonify(data)

@bp.route('/uploadmedia',methods=['GET','POST'])
def uploadfile():
     imageFolder = 'media/'
     myimage = request.files.get("file")
     fname= myimage.filename
     fp=os.path.join(imageFolder,fname)
     myimage.save(fp)
     data={
          "location": '../media/'+fname
     }  
     return jsonify(data)


@bp.route('/savecontent',methods=['POST'])
def savecontent():
     article_id = request.form['article_id']
     title = request.form['title']
     content = request.form['content']
     state = request.form['state']
     hostid = request.form['hostid']
     departid = request.form['departid']
     if(g.user is not None):
          insert_article(article_id,title,content,session.get('nl_user_id'),state,hostid,departid)
     else:
          insert_article(article_id,title,content,0,state,hostid,departid)
     return render_template('articlelist.html')


@bp.route('/articlelist',methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def articlelist():
    return render_template('articlelist.html')


@bp.route('/articledata',methods=['GET'])   #管理编辑页面用
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def articleData():
    data = []
    articlelist = get_all_article()
    idx = 0
    for article in articlelist:
        idx = idx+1
        p={}
        p['index']=idx
        p['article_id']=article[0].article_id
        p['title']=article[0].title
        p['ownerid']=article[0].ownerid
        if(article[0].state == '0'):
            p['ispublish']="未发布"
        elif(article[0].state == '1'):
            p['ispublish']="已发布"
        p['createtime']=article[0].createtime.strftime("%Y-%m-%d %H:%M:%S")
        if(article[0].modifytime is not None):
            p['modifytime']=article[0].modifytime.strftime("%Y-%m-%d %H:%M:%S")
        else:
            p['modifytime']=''
        p['readcountnum']=article[1]

        data.append(p)
    table_data  = {'total': 1,'rows':data}
    return jsonify(table_data)

@bp.route('/articlesimpledata',methods=['GET']) #用户显示页面用，额外加工数据
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def articleSimpleData():
    data = []
    articlelist = get_all_article_filterbystate()
    
    idx = 0
    for article in articlelist:
        idx = idx+1
        p={}
        #p['index']=idx
        #p['article_id']=article.article_id
        if(article[0] is None):break
        p['title']=article[0].title
        #p['ownerid']=article.ownerid
        if(article[0].modifytime is not None):
          p['time']=article[0].modifytime.strftime("%Y-%m-%d %H:%M:%S")
        else:
          p['time']=article[0].createtime.strftime("%Y-%m-%d %H:%M:%S")
        if(article[0].content is None):
            content = ''
        else:
            content = article[0].content
            content = HTMLParser(content).text()   #去除标签
            content = content.replace('\n','')
        p['content'] = content
        p['url']='article?article_id='+str(article[0].article_id)
        p['readcountnum']=article[1]
        data.append(p)
    table_data  = {'total': 1,'rows':data}
    return jsonify(table_data)



@bp.route('/edit_article')
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def editarticle():
    article_id = request.args.get("article_id")
    article = get_article_byid(article_id)[0]
    article_data={'article_id' : article_id,'title':article[0].title,'content':article[0].content,\
                  'hostid':article[0].hostid,'departid':article[0].departmentid}
    flash(article_data)
    users = get_alluser()
    userlist = []
    for item in users:
        namepylist = pypinyin.pinyin ( item.username, style=pypinyin.FIRST_LETTER)
        namepy = ''.join(i[0] for i in namepylist)
        userlist.append({'userid':item.userid,'name':item.username,'py':namepy})

    departments = get_alldepartment()
    departmentlist = []
    for item in departments:
        departnamelist = pypinyin.pinyin ( item.departmentname, style=pypinyin.FIRST_LETTER)
        departpy = ''.join(i[0] for i in departnamelist)
        departmentlist.append({'departmentid':item.departmentid,'name':item.departmentname,'py':departpy})
    return render_template('publishinform.html',userlist=userlist,departmentlist= departmentlist)


@bp.route('/deletearticle', methods=['GET', 'POST'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def deletearticle():
    article_id = request.form['article_id']
    delete_article(article_id)
    return render_template('articlelist.html')


@bp.route('/mreadarticlelst', methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def showreadarticlelist():
    return render_template('mobile/mobile_readarticlelist.html')


@bp.route('/article', methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def showarticle():
    article_id = request.args.get("article_id")
    article = get_article_byid(article_id)[0]
    
    if(article[0].modifytime is None):
        article[0].modifytime = article[0].createtime.strftime("%Y-%m-%d %H:%M:%S")
    else:
        article[0].modifytime = article[0].modifytime.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('article_page.html',article=article[0],readcountnum = article[1])


@bp.route('/recordread', methods=['post'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def recordread():
    article_id = request.form['id']
    userid = session.get('nl_user_id') 
    readrecord=get_user_readrecord(userid)
    firstreadflag = 1
    for r in readrecord:
        if(r.articleid == int(article_id)):
            firstreadflag=0
    if(firstreadflag):
        insert_readrecord(article_id,userid,1)
    return render_template('/index.html')
