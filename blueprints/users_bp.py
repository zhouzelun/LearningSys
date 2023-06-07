from flask import Blueprint,render_template,g,flash,jsonify,request,session,redirect
from database import get_user_scores,get_user_answerrecord,get_paper_byid,get_user_bysession,get_user_readrecord,\
    get_article_byid,alterpassword
from permission import Permissions,permission_required
bp = Blueprint("users_bp",__name__,url_prefix="/user")

@bp.route("/home")
@permission_required(Permissions.USER_PERMISSION)
def showusercenter():
    user_info = []
    if hasattr(g,'user') and g.user is not None:
        userscore = list(get_user_scores(g.user.userid)[0])
        #answerrecord = get_user_answerrecord(g.user.userid)
        current_user = get_user_bysession()
        info = {}
        info['userscore'] = userscore
        info['username'] = current_user.username
        user_info.append(info)
        # for item in answerrecord:
        #     info = {}
        #     info['paperid'] = item[0].paperid
        #     info['insertdate'] = item[0].insertdate.strftime('%Y-%m-%d %H:%M:%S')
        #     user_info.append(info)
        flash(user_info)
    return render_template("usercenter.html")


@bp.route("/alterpassword",methods=['GET', 'POST'])
@permission_required(Permissions.USER_PERMISSION)
def alteruserpassword():
    if request.method == 'GET':
        return render_template("alterpassword.html")
    elif request.method == 'POST':
        repeatnewpass = request.form.get('repeatnewpass')
        newpass = request.form.get('newpass')
        flag = alterpassword(session.get('nl_user_id'),newpass)
        return redirect('/loginout')

@bp.route('/answerdata',methods=['GET', 'POST'])
@permission_required(Permissions.USER_PERMISSION)
def answerdata():
    user_info = []
    if hasattr(g,'user') and g.user is not None:
        answerrecord = get_user_answerrecord(g.user.userid)
        info = {}
        idx = 0
        for item in answerrecord:
            paper_info = get_paper_byid(item[0].paperid)
            idx = idx+1
            info = {}
            info['index'] = idx
            info['papername'] = paper_info[0].paper_title
            info['score'] = item[0].getmark
            info['insertdate'] = item[0].insertdate.strftime('%Y-%m-%d %H:%M:%S')
            if(item[1] is not None):
                info['score_1'] = item[1].score_1
                info['score_2'] = item[1].score_2
                info['score_3'] = item[1].score_3
            user_info.append(info)
    table_data  = {'total': 2,'rows':user_info}
    return jsonify(table_data)

@bp.route('/readdata',methods=['GET', 'POST'])
@permission_required(Permissions.USER_PERMISSION)
def readdata():
    user_info = []
    if hasattr(g,'user') and g.user is not None:
        readrecord = get_user_readrecord(g.user.userid)
        info = {}
        idx = 0
        for item in readrecord:
            article_info = get_article_byid(item[0].articleid)
            idx = idx+1
            info = {}
            info['index'] = idx
            info['title'] = article_info[0][0].title
            info['insertdate'] = item[0].insertdate.strftime('%Y-%m-%d %H:%M:%S')
            if(item[1] is not None):
                info['score_1'] = item[1].score_1
                info['score_2'] = item[1].score_2
                info['score_3'] = item[1].score_3
            user_info.append(info)
    table_data  = {'total': 2,'rows':user_info}
    return jsonify(table_data)


