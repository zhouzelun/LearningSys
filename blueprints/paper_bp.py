from flask import Blueprint,render_template,g
from flask import Flask, jsonify,request,flash
from flask import session
from database import  get_paper_byid, insert_paper,get_user_answerrecord,paper_hasanswer,\
    get_paper_questions_byid, insert_record,get_all_paper_filterbystate,get_alluser,get_alldepartment,drop_paper,insert_scorerecord,\
    get_all_paper_filterbystate_user,unlockpaper,get_answerrecord_bypaper
from permission import Permissions,permission_required
import pypinyin

bp = Blueprint("paper",__name__,url_prefix="/paper")
@bp.route('/list',methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def showPaperList():
    return render_template('paperlist.html')
    '''elif request.method=='POST':
        data = []
        paperlist = get_all_paper()
        for paper in paperlist:
            p={}
            p['paperid']=paper.paperid
            p['paper_title']=paper.paper_title
            p['ownerid']=paper.ownerid
            p['createtime']=paper.createtime
            p['modifytime']=paper.modifytime
            p['question_count']=paper.question_count
            data.append(p)
        tabele_data  = {'total': 1,'rows':data}
        return jsonify(tabele_data)'''


@bp.route('/paperdata/state=<statelist>',methods=['GET'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def paperData(statelist):
    data = []
    paperlist = get_all_paper_filterbystate_user(statelist.split(','),session.get('nl_user_id'))
    idx = 0
    for paper in paperlist:
        idx = idx+1
        p={}
        p['index']=idx
        p['paperid']=paper.paperid
        p['paper_title']=paper.paper_title
        p['ownerid']=paper.ownerid
        p['createtime']=paper.createdate.strftime("%Y-%m-%d %H:%M:%S")
        if(paper.modifydate is not None):
            p['modifytime']=paper.modifydate.strftime("%Y-%m-%d %H:%M:%S")
        else:
            p['modifytime']=''
        p['question_count']=paper.quetion_count
        if(paper.state =='1'):
            p['ispublish']="已发布"
        else:
            p['ispublish']="未发布"
        p['question_count']=paper.quetion_count
        p['hasanaser'] = paper_hasanswer(session.get('nl_user_id'),paper.paperid)
        data.append(p)
    table_data  = {'total': 1,'rows':data}
    return jsonify(table_data)


def getusersanddepars():
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
    return userlist,departmentlist


@bp.route('/create_paper', methods=['GET', 'POST'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def createPaper():
    if request.method=='GET':
        userlist,departmentlist=getusersanddepars()
        return render_template('create_paper.html',userlist=userlist,departmentlist= departmentlist)
    elif request.method=='POST':
        all_data = request.form.getlist('all_data[]')    #试卷上所有题目 返回的格式是一道题目一个列表项，题目中以|分隔，依次为
                                                         #题目、是否选择A(1是选择了，0是没选择)、选项A内容........
        paper_title = request.form['paper_title']    #试卷标题
        paper_owner = request.form['paper_owner']    #0:所有人   1:个人的
        paper_id = request.form['paper_id'] 
        quetion_count = request.form['quetion_count']
        state = request.form['state']
        hostid = request.form['hostid']
        departid = request.form['departid']
        #if(paper_owner=='1' and g.user is not None):
        insert_paper(paper_title,paper_id,quetion_count,state,session.get('nl_user_id'),all_data,int(hostid),departid)
        
        return jsonify("refresh") 



@bp.route('/edit_paper')
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def editPaper():
    paper_id = request.args.get("paper_id")
    papers = []
    paper_qustions = get_paper_questions_byid(paper_id)
    paper_info = get_paper_byid(paper_id)
    p={}
    p['paper_title']=paper_info[0].paper_title
    p['paper_id']=paper_info[0].paperid
    p['ownerid']=paper_info[0].ownerid
    p['hostid']=paper_info[0].hostid
    p['departid']=paper_info[0].departmentid
    papers.append(p)
    for question in paper_qustions:
        p={}
        p['questionid']=question.questionid
        p['paperid']=question.paperid
        p['detail']=question.detail
        p['type']=question.type
        p['mark']=question.mark
        papers.append(p)
    flash(papers)
    userlist,departmentlist=getusersanddepars()
    return render_template('create_paper.html',userlist=userlist,departmentlist= departmentlist)
    


@bp.route('/answer')
@permission_required(Permissions.USER_PERMISSION)
def answer():
    paper_id = request.args.get("paper_id")
    if(paper_hasanswer(session.get('nl_user_id'),paper_id) != -1):
        return render_template('answerpaperlist.html')
    papers = []
    paper_qustions = get_paper_questions_byid(paper_id)
    paper_info = get_paper_byid(paper_id)
    p={}
    p['paper_title']=paper_info[0].paper_title
    p['paper_id']=paper_info[0].paperid
    p['ownerid']=paper_info[0].ownerid
    
    papers.append(p)
    for question in paper_qustions:
        p={}
        p['questionid']=question.questionid
        p['paperid']=question.paperid
        p['detail']=question.detail
        p['type']=question.type
        p['mark']=question.mark
        papers.append(p)
    flash(papers)
    insert_record(paper_id,session.get('nl_user_id'),0,0)
    return render_template('answer_paper.html')



@bp.route('/write_result', methods=['GET', 'POST'])
@permission_required(Permissions.USER_PERMISSION)
def get_result():
    paper_id = request.form['paper_id'] 
    correct_count = request.form['correct_count'] 
    userid = session.get('nl_user_id') 
    recordid = insert_record(paper_id,session.get('nl_user_id'),1,correct_count)
    return render_template('answerpaperlist.html')



@bp.route('/deletepaper', methods=['GET', 'POST'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def deletepaper():
    paper_id = request.form['paper_id']
    drop_paper(paper_id)
    return render_template('paperlist.html')

@bp.route('/unlockpaper', methods=['GET', 'POST'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def unlockuserpaper():
    if request.method=='GET':
        data=[]
        paperlist = get_all_paper_filterbystate([0,1])
        for paper in paperlist:
            p={}
            p['paperid']=paper.paperid
            p['paper_title']=paper.paper_title
            titlepylist = pypinyin.pinyin (paper.paper_title, style=pypinyin.FIRST_LETTER)
            titlepy = ''.join(i[0] for i in titlepylist)
            p['py']=titlepy
            data.append(p)
        return render_template('lockpaperlist.html',data=data)
    elif request.method=='POST':
        answerid = request.form['answerid']
        unlockpaper(answerid)
        return render_template('paperlist.html')

@bp.route('/lockuserdata', methods=['GET','POST'])
@permission_required(Permissions.MANAGEMENT_PERMISSION)
def lockuserdata():
    paper_id = request.args.get("paper_id")
    answerrecord = get_answerrecord_bypaper(paper_id)
    data = []
    for record in answerrecord:
        p={}
        p['answerid']=record[0].recordid
        p['workid']=record[1].workid
        p['username']=record[1].username
        p['insertdate']=record[0].insertdate.strftime("%Y-%m-%d %H:%M:%S")
        data.append(p)
    return jsonify(data)

@bp.route('/answerpaperlist')
@permission_required(Permissions.USER_PERMISSION)
def showanserpaperlist():
    return render_template('answerpaperlist.html')
    '''elif request.method=='POST':
        data = []
        paperlist = get_all_paper()
        for paper in paperlist:
            p={}
            p['paperid']=paper.paperid
            p['paper_title']=paper.paper_title
            p['ownerid']=paper.ownerid
            p['createtime']=paper.createtime
            p['modifytime']=paper.modifytime
            p['question_count']=paper.question_count
            data.append(p)
        tabele_data  = {'total': 1,'rows':data}
        return jsonify(tabele_data)'''
        