from flask import Blueprint, render_template,request,redirect,flash
from permission import Permissions,permission_required
from flask import current_app,jsonify,session,g
from database import insert_article,get_all_article,get_article_byid,\
insert_readrecord,get_user_readrecord,get_all_article_filterbystate,get_alluser,get_alldepartment,\
user_hasread,drop_article,get_all_article_filterbystate_user,updatefile,getfile_byarticleid
import os
from selectolax.parser import HTMLParser
import pypinyin
from urllib.parse import quote
import base64
import config
bp = Blueprint("information",__name__,url_prefix="/information")


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
          "location": '../files/getfile/images/'+fname
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
          "location": '../files/getfile/media/'+fname
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
    filekeys = request.values.getlist('filekeys[]')
    if(g.user is not None):
         article_id=insert_article(article_id,title,content,session.get('nl_user_id'),state,hostid,departid)
    else:
         article_id=insert_article(article_id,title,content,0,state,hostid,departid)
    #insert_scorerecord(session.get('nl_user_id'),0,2,0,2,articleid=article_id)
    for key in filekeys:
        updatefile(key,article_id)
    return render_template('articlelist.html')


@bp.route('/articlelist',methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def articlelist():
    return render_template('articlelist.html')


@bp.route('/articledata',methods=['GET'])   #管理编辑页面用
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def articleData():
    data = []
    articlelist = get_all_article_filterbystate_user(session.get('nl_user_id'))
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
        p['hasread']= user_hasread(session.get('nl_user_id'),article[0].article_id)
        data.append(p)
    table_data  = {'total': 1,'rows':data}
    return jsonify(table_data)

@bp.route('/edit_article')
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def editarticle():
    article_id = request.args.get("article_id")
    article = get_article_byid(article_id)[0]
    fileconfig={'config':[],'content':[]}
    files = getfile_byarticleid(article_id)
    for file in files:
        fname = file.path.split('/')[-1]
        file_type=['word','primary']
        if file.type == '0':
            file_type=['word','primary']
        elif file.type == '1':
            file_type=['excel','success']
        elif file.type == '2':
            file_type=['powerpoint','danger']
        elif file.type == '3':
            file_type=['pdf','danger']
        fileconfig['content'].append('<i class="fas fa-file-{} fa-2xl text-{}"></i>'.format(file_type[0],file_type[1]))
        fileconfig['config'].append({'caption':fname,'url':'/files/deletefile','type':'image','key':file.fileid})
    article_data={'article_id' : article_id,'title':article[0].title,'content':article[0].content,\
                  'hostid':article[0].hostid,'departid':article[0].departmentid,'fileconfig':fileconfig}

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
    drop_article(article_id)
    return render_template('articlelist.html')


@bp.route('/readarticlelist', methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def showreadarticlelist():
    return render_template('readarticlelist.html')


@bp.route('/article', methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def showarticle():
    hosturl = request.host_url
    filepreviewurl =request.host_url.replace('5000', '8012')
    article_id = request.args.get("article_id")
    article = get_article_byid(article_id)[0]
    files = getfile_byarticleid(article_id)
    filelist = []
    
    for index,file in enumerate(files):
        f={}
        f['index']=index
        f['fname']=file.path.split('/')[-1]
        # laststr = base64.b64encode((hosturl+"/files/getfile/"+file.path).encode())
        f['url']=file.path
        match file.type:
            case '0':f['type']=['word','primary']
            case '1':f['type']=['excel','success']
            case '2':f['type']=['powerpoint','danger']
            case '3':f['type']=['pdf','danger']
        filelist.append(f)
    if(article[0].modifytime is None):
        article[0].modifytime = article[0].createtime.strftime("%Y-%m-%d %H:%M:%S")
    else:
        article[0].modifytime = article[0].modifytime.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('article_page.html',article=article[0],readcountnum = article[1],\
                filelist=filelist,hosturl=config.hosturl,filepreviewurl=config.filepreviewurl)


@bp.route('/recordread', methods=['post'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def recordread():
    article_id = request.form['id']
    userid = session.get('nl_user_id') 
    readrecord=get_user_readrecord(userid)
    firstreadflag = 1
    for r in readrecord:
        if(r[0].articleid == int(article_id)):
            firstreadflag=0
    if(firstreadflag):
        readid = insert_readrecord(article_id,userid)
        #insert_scorerecord(session.get('nl_user_id'),1,0,0,0,readid=readid)
    return render_template('/index.html')
