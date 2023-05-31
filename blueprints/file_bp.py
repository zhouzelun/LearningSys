
from flask import Blueprint, render_template,request,send_file,g
import os
from datetime import datetime
import json
from database import deletefile,insertfile


bp = Blueprint("files",__name__,url_prefix="/files")



@bp.route('/uploadfile',methods=['GET','POST'])
def uploadfile():
    current_user = g.user
    if (request.method == 'GET'):
        return render_template('uploadfiles.html')
    elif request.method == 'POST':
        one_file = request.files.get("input-folder-3[]")
        fileFolder = 'learningfilestorage/'+current_user.workid+'/'+ datetime.now().strftime("%Y-%m")
        fname= one_file.filename
        fp=os.path.join(fileFolder,fname)
        if not os.path.exists(fileFolder):
            os.makedirs(fileFolder)
        while os.path.exists(fp):#如果重名 在文件前面加_
            fname = '_'+fname
            fp=os.path.join(fileFolder,fname)
        file_type=''  #判断文件格式，给前端返回不同的图标
        type = 0
        if fname.split('.')[-1] == 'doc' or fname.split('.')[-1] == 'docx':
            file_type=['word','primary']
            type=0
        elif fname.split('.')[-1] == 'xls' or fname.split('.')[-1] == 'xlsx':
            file_type=['excel','success']
            type=1
        elif fname.split('.')[-1] == 'ppt' or fname.split('.')[-1] == 'pptx':
            file_type=['powerpoint','danger']
            type=2
        elif fname.split('.')[-1] == 'pdf':
            file_type=['pdf','danger']
            type=3
        one_file.save(fp)  
        fileid = insertfile(fp,type)
        responsedata = {
            'initialPreview': ['<i class="fas fa-file-{} fa-2xl text-{}"></i>'.format(file_type[0],file_type[1])],
            'append': True ,
            'initialPreviewAsData': True,
            'initialPreviewFileType': 'image',
            'initialPreviewConfig':[{'caption': fname, 'url': "/files/deletefile", 'key': fileid}]
        }
        d = json.dumps(responsedata)
        return d


@bp.route('deletefile',methods=['GET','POST'])
def postdeletefile():
    fileid = request.form.get('key')
    deletefile(fileid)
    responsedata = {
            'append': True 
    }
    d = json.dumps(responsedata)
    return d




@bp.route('getfile/<path:url_path>/<file_name>', methods=['GET']) #泛型
def get_file(url_path,file_name):
    file_path = os.path.join(url_path, file_name)
    return send_file(file_path)