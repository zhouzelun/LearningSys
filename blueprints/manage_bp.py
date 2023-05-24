from flask import Blueprint,render_template,g
from flask import Flask, jsonify,request,flash
from flask import session
from database import  insert_scorerecord,get_alluser
from permission import Permissions,permission_required
import pypinyin

bp = Blueprint("manage",__name__,url_prefix="/manage")

@bp.route("/insertscore", methods=['post','get'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def insertscore():
    if request.method=='POST':
        userid = request.form['userid'] 
        score_1 = request.form['score_1'] 
        score_2 = request.form['score_2'] 
        score_3 = request.form['score_3'] 
        insert_scorerecord(userid,score_1,score_2,score_3,3)
        return jsonify({'update':'ok'})
    else:
        users = get_alluser()
        userlist = []
        for item in users:
            namepylist = pypinyin.pinyin ( item.username, style=pypinyin.FIRST_LETTER)
            namepy = ''.join(i[0] for i in namepylist)
            userlist.append({'userid':item.userid,'name':item.username,'py':namepy})
        return render_template("add_score.html",userlist=userlist)