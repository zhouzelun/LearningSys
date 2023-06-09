from datetime import datetime
from sqlalchemy import create_engine,CHAR, TEXT, VARCHAR, Column,ForeignKey,Integer,select,DateTime ,update
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from flask import session as flask_session
from sqlalchemy.sql import func
import config
Base = declarative_base()
#alembic revision --autogenerate -m  "addfilemanagmentforecol";  
#alembic upgrade head
class Role(Base):
    __tablename__ = "ROLE"
    roleid = Column(Integer, primary_key=True)
    rolename = Column(VARCHAR(30))
    rolepower =  Column(Integer)
    def __repr__(self):
        return f"Role(roleid={self.roleid!r}, name={self.rolename!r},rolepower={self.rolepower!r})"

class User(Base):
    __tablename__ = "USER"
    userid = Column(Integer, primary_key=True)
    roleid = Column(Integer, ForeignKey("ROLE.roleid"))
    departmentid = Column(Integer, ForeignKey("DEPARTMENT.departmentid"))
    workid = Column(VARCHAR(10))
    username = Column(VARCHAR(30))
    sex = Column(CHAR)
    password = Column(VARCHAR(32))
    def __repr__(self):
        return f"user(userid={self.userid!r},workid={self.workid!r},roleid={self.roleid!r},username={self.username!r},sex={self.sex!r},password={self.password!r})"

class Paper(Base):
    __tablename__ = "PAPER"
    paperid = Column(Integer, primary_key=True)
    paper_title = Column(TEXT)
    ownerid = Column(Integer)
    hostid = Column(Integer, ForeignKey("USER.userid"))
    departmentid = Column(Integer, ForeignKey("DEPARTMENT.departmentid"))
    createdate = Column(DateTime)
    modifydate = Column(DateTime)
    state = Column(CHAR)         #记录状态
    quetion_count = Column(Integer)
    questions = relationship("Question", back_populates="paper", cascade="all, delete")
    answerecords = relationship("AnswerRecord", back_populates="paper")
    def __repr__(self):
        return f"Paper(paperid={self.paperid!r},paper_title={self.paper_title!r},ownerid={self.ownerid!r})"

class Question(Base):
    __tablename__ = "QUESTION"
    questionid = Column(Integer, primary_key=True)
    paperid = Column(Integer, ForeignKey("PAPER.paperid"), nullable=False)
    type = Column(CHAR)
    detail = Column(TEXT)
    paper = relationship("Paper", back_populates="questions")
    mark = Column(Integer)
    def __repr__(self):
        return f"Question(questionid={self.questionid!r},paperid={self.paperid!r},type={self.type!r},detail={self.detail!r})"

class AnswerRecord(Base):
    __tablename__ = "ANSWERRECORD"
    recordid =  Column(Integer, primary_key=True)
    userid =  Column(Integer, ForeignKey("USER.userid"), nullable=False)
    paperid = Column(Integer, ForeignKey("PAPER.paperid"), nullable=False)
    insertdate = Column(DateTime)
    paper = relationship("Paper", back_populates="answerecords")
    state = Column(CHAR)
    getmark = Column(Integer)
    def __repr__(self):
        return f"AnswerRecord(userid={self.userid!r},paperid={self.paperid!r},insertdate={self.insertdate!r})"


class ReadRecord(Base):
    __tablename__ = "READRECORD"
    readid =  Column(Integer, primary_key=True)
    userid =  Column(Integer, ForeignKey("USER.userid"), nullable=False)
    articleid = Column(Integer, ForeignKey("ARTICLE.article_id"), nullable=False)
    insertdate = Column(DateTime)
    article = relationship("Article", back_populates="readrecords")
    def __repr__(self):
        return f"AnswerRecord(userid={self.userid!r},articleid={self.articleid!r},insertdate={self.insertdate!r})"

class Article(Base):
    __tablename__ = "ARTICLE"
    article_id =  Column(Integer, primary_key=True)
    title  = Column(VARCHAR(100))
    hostid = Column(Integer)   
    departmentid = Column(Integer, ForeignKey("DEPARTMENT.departmentid"))
    content = Column(TEXT)
    createtime = Column(DateTime)
    modifytime = Column(DateTime)
    ownerid = Column(Integer, ForeignKey("USER.userid"), nullable=False)
    state = Column(CHAR)
    readrecords = relationship("ReadRecord", back_populates="article")
    files = relationship("File", back_populates="article")
    def __repr__(self):
        return f"Article(article_id={self.article_id!r},title={self.title!r},content={self.content!r},ownerid={self.ownerid!r})"

class ScoreRecord(Base):
    __tablename__ = "SCORERECORD"
    recordid = Column(Integer, primary_key=True)
    userid =  Column(Integer, ForeignKey("USER.userid"), nullable=False)
    score_1 = Column(Integer)
    score_2 = Column(Integer)   
    score_3 = Column(Integer)   
    comefrom = Column(CHAR) #0 是看文章来的 1是答题来的 2发布文章来的 3是额外插入的
    answerid =Column(Integer,ForeignKey("ANSWERRECORD.recordid"))
    readid =Column(Integer,ForeignKey("READRECORD.readid"))
    articleid =Column(Integer,ForeignKey("ARTICLE.article_id"))
    insertdate = Column(DateTime)

class Department(Base):
    __tablename__ = "DEPARTMENT"
    departmentid = Column(Integer, primary_key=True)
    departmentname =  Column(VARCHAR(100))

class File(Base):
    __tablename__ = "FILE"
    fileid = Column(Integer, primary_key=True)
    path =  Column(TEXT)
    articleid=Column(Integer, ForeignKey("ARTICLE.article_id"))
    type=Column(CHAR) #0 word 1 excel 2 ppt 3 pdf 
    article = relationship("Article", back_populates="files")
    insertdate = Column(DateTime)


engine = create_engine(config.DB_URI)

Base.metadata.create_all(engine)


def initdata():
    with Session(engine) as session:
        Rolelist = [Role(
            roleid = 1,
            rolename='management',
            rolepower=255
            ),Role(
            roleid = 2,
            rolename='user',
            rolepower=2
            )]
        session.add_all(Rolelist)
        departlist = [
            Department(
                departmentid=1,
                departmentname='测试科室'
            )
            ]
        session.add_all(departlist)
        userlist = [User(
                roleid = 1,
                departmentid=1,
                username='管理员',
                workid='001',
                sex=1,
                password='123456'
            ),User(
                roleid = 2,
                departmentid=1,
                username='测试用户啊',
                workid='002',
                sex=1,
                password='123456'
            )
            ]
        session.add_all(userlist)
        session.commit()
        


def get_alluser():    #获取所有用户
    with Session(engine) as session:
        stmt = select(User)
        result =  session.execute(stmt)
        return result.scalars().all()


def get_user_byid(id):    #通过id获取用户
    with Session(engine) as session:
        stmt = select(User).where(User.userid==id)
        result =  session.execute(stmt)
        login_user = result.first()
        return login_user

def get_user_byloginname(loginname):      #通过工号workid获取用户
    with Session(engine) as session:
        stmt = select(User).where(User.workid==loginname)
        result =  session.execute(stmt)
        login_user = result.first()
        return login_user

def get_all_paper():              #获取所有试卷
    stmt = select(Paper)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()
    
def get_all_paper_filterbystate(statelist):         #根据试卷状态获取    
    stmt = select(Paper).where(Paper.state.in_(statelist))
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()
    
def get_all_paper_filterbystate_user(statelist,ownerid):       #根据试卷状态和拥有者的id获取试卷         
    stmt = select(Paper).where(Paper.state.in_(statelist),Paper.ownerid==ownerid)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()

def get_paper_byid(paper_id):   #根据试卷id获取试卷
    stmt = select(Paper).where(Paper.paperid == paper_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()

def get_paper_questions_byid(paper_id):   #获取question 根据试卷id
    stmt = select(Question).where(Question.paperid == paper_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()



def get_role_byuser(current_user): #根据现在用户获取他的角色
    role_id=2                      #默认为匿名用的id
    if(current_user is not None):
        role_id = current_user.roleid
    with Session(engine) as session:
        role = session.query(Role).filter_by(roleid=role_id).first()
        return role

def get_user_bysession():     #直接根据session里的id获取用户
    with Session(engine) as session:
        u = session.query(User).filter_by(userid=flask_session.get('nl_user_id')).first()
        return u

def get_user_scores(id):     #根据用户的id获取该用户所有的积分
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(func.sum(ScoreRecord.score_1).label("score1"),func.sum(ScoreRecord.score_2).label("score2"),func.sum(ScoreRecord.score_3).label("score3")).filter_by(userid=id)
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result

def get_user_answerrecord(id):    #根据用户的id获取该用户所有的答题记录
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(AnswerRecord,ScoreRecord).filter_by(userid=id).filter(AnswerRecord.state != 2)\
        .outerjoin(ScoreRecord)\
        .order_by(AnswerRecord.insertdate.desc())
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result

def get_answerrecord_bypaper(id):#根据试卷id获取试卷的答题记录
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(AnswerRecord,User).filter_by(paperid=id).filter(AnswerRecord.state != 2)\
        .outerjoin(User)\
        .order_by(AnswerRecord.insertdate.desc())
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result
    
def get_user_readrecord(id):      #根据用户的id获取该用户所有的阅读记录
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(ReadRecord,ScoreRecord).filter_by(userid=id)\
        .outerjoin(ScoreRecord)\
        .order_by(ReadRecord.insertdate.desc())
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result
    
def get_all_readrecord():     #获取所有的阅读记录
#stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(ReadRecord)
    with Session(engine) as session:
        result =  session.execute(stmt).scalars().all()
        return result


def get_all_article():     #获取所有的文章
    stmt = select(Article,func.count(ReadRecord.readid)).outerjoin(ReadRecord).group_by(Article.article_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.all()
    
def get_all_article_filterbystate():      #筛选已发布的文章
    stmt = select(Article,func.count(ReadRecord.readid)).outerjoin(ReadRecord).where(Article.state==1).group_by(Article.article_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.all()
    

def get_all_article_filterbystate_user(ownerid):     #根据所有者筛选文章
    stmt = select(Article,func.count(ReadRecord.readid)).outerjoin(ReadRecord).\
        where(Article.state==1,Article.ownerid==ownerid).group_by(Article.article_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.all()
    
def get_all_article_bak():    
    stmt = select(Article)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()
    
#scalars()返回每个row对象的第一个元素
def get_article_byid(article_id): #根据文章id返回文章
    stmt = select(Article,func.count(ReadRecord.readid)).\
        outerjoin(ReadRecord).where(Article.article_id == article_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.all()

def getfile_byarticleid(articleid):#根据文章id返回文章下的所有文件
    stmt = select(File).where(File.articleid == articleid)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()
    
    
def get_alldepartment():#获取所有部门
    with Session(engine) as session:
        stmt = select(Department)
        result =  session.execute(stmt)
        return result.scalars().all()
    


def delete_paper(paper_id):#直接删除试卷
    with Session(engine) as session:
        paper = session.query(Paper).filter_by(paperid=paper_id).first()
        if (paper is not None):
            session.delete(paper)
            session.commit()
            return paper
    return None

def drop_paper(paper_id):#改试卷状态作废
    with Session(engine) as session:
        stmt=update(Paper).where(Paper.paperid==paper_id).values(state=2)
        session.execute(stmt)
        paper = session.query(Paper).filter_by(paperid=paper_id).first()
        return paper

def delete_question_bypaperid(paper_id):#删除题目
    with Session(engine) as session:
        Questions = session.query(Question).filter_by(paperid=paper_id)
        if (Questions is not None):
            for q in Questions:
                session.delete(q)
            session.commit()


def insert_question(paper_id,type,detail,mark):#插入题目
    with Session(engine) as session:
        one_question = Question(
                paperid = paper_id,
                type=type,
                detail=detail,
                mark=mark
        ) 
        session.add_all([one_question])
        session.commit()

def insert_paper(_paper_title,paper_id,count,paper_state,_ownerid,_questions,hostid,departmentid):#插入试卷
    p = drop_paper(paper_id)#先把试卷作废 state变成2 主要判断是否是None
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with Session(engine) as session:
        if(p is not None):
            delete_question_bypaperid(paper_id)#删除其下所有question
            for item in _questions:#重新插入新的question
                insert_question(paper_id,item.split('|')[0],detail = item[2:-1],mark = item.split('|')[-1])
            stmt=update(Paper).where(Paper.paperid==paper_id).values(hoistid=hostid,departmentid=departmentid,modifydate=now_time,state=paper_state,paper_title=_paper_title,ownerid=_ownerid,quetion_count=count)
            session.execute(stmt)
            session.commit()
            '''one_paper = Paper(
                paperid = p.paperid,
                createdate = p.createdate,
                modifydate = now_time,
                state = paper_state,
                paper_title=_paper_title,
                ownerid=_ownerid,
                questions=ques_list,
                quetion_count = count
            )   '''
        else:
            ques_list = []
            for item in _questions:#重新插入新的question
                ques_list.append(
                Question(
                    type = item.split('|')[0],
                    detail = item[2:],
                    mark = item.split('|')[-1]
                )
                )
            one_paper = Paper(
                createdate = now_time,
                state = paper_state,
                departmentid=departmentid,
                paper_title=_paper_title,
                ownerid=_ownerid,
                hostid=hostid,
                questions=ques_list,
                quetion_count = count
            ) 
            session.add_all([one_paper])
            session.commit()
    return True  

def drop_answerrecord(paper_id:int,user_id:int): #作废回答记录 用于解锁用户的答题
    with Session(engine) as session:
        stmt=update(AnswerRecord).where(AnswerRecord.paperid==paper_id,AnswerRecord.userid==user_id).values(state=2)
        session.execute(stmt)
        #record = session.query(AnswerRecord).filter_by(paperid=int(paper_id),userid=user_id).filter(AnswerRecord.state!=2).first()
        session.commit()
        return True



def insert_record(paper_id,user_id,state,getmark): #插入答题记录
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with Session(engine) as session:
        one_record = session.query(AnswerRecord).filter_by(paperid=int(paper_id),userid=user_id).filter(AnswerRecord.state!=2).first()
        if one_record is not None:
            stmt=update(AnswerRecord).where(AnswerRecord.paperid==paper_id,AnswerRecord.userid==user_id).\
            filter(AnswerRecord.state!=2).\
            values(state=state,getmark=getmark,insertdate = now_time)
            session.execute(stmt)
        else:
            one_record = AnswerRecord(
            paperid = paper_id,
            userid =  user_id,
            insertdate = now_time,
            state = state,
            getmark = getmark
            )
            session.add(one_record)
            session.flush()
        if(~hasrecordscore(flask_session.get('nl_user_id'),1,answerid=one_record.recordid)):
            one_scorerecord=None
            if((getmark is None) or int(getmark)<80):
                pass
            elif(int(getmark)<90):
                one_scorerecord=new_scorerecord(flask_session.get('nl_user_id'),2,0,0,1,answerid=one_record.recordid)
                session.add(one_scorerecord)
            else:
                one_scorerecord=new_scorerecord(flask_session.get('nl_user_id'),2,2,0,1,answerid=one_record.recordid)
                session.add(one_scorerecord)
        session.commit()
    return True


def insert_readrecord(article_id,user_id): #插入阅读记录
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with Session(engine) as session:
        one_record = ReadRecord(
            articleid = article_id,
            userid =  user_id,
            insertdate = now_time
        )
        session.add(one_record)
        session.flush()
        if(~hasrecordscore(flask_session.get('nl_user_id'),2,readid=one_record.readid)):
            session.add(new_scorerecord(flask_session.get('nl_user_id'),1,0,0,0,readid=one_record.readid))
        session.commit()
        return one_record.readid  


def delete_article(article_id): #删除文章
    with Session(engine) as session:
        article = session.query(Article).filter_by(article_id=article_id).first()
        if (article is not None):
            session.delete(article)
            session.commit()
            return article
    return None

def drop_article(article_id):#作废文章
    with Session(engine) as session:
        with Session(engine) as session:
            stmt=update(Article).where(Article.article_id==article_id).values(state=2)
            session.execute(stmt)
            article = session.query(Article).filter_by(article_id=article_id).first()
            session.commit()
            return article


def insert_article(article_id,title,content,ownerid,state,hostid,departmentid): #插入文章
    if(hostid==''):hostid=None
    if(departmentid==''):departmentid=None
    p = drop_article(article_id)
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with Session(engine) as session:
        if(p is not None):
            stmt=update(Article).where(Article.article_id==article_id).values(content=content,hostid=hostid,departmentid=departmentid,modifytime=now_time,state=state,title=title,ownerid=ownerid)
            session.execute(stmt)
            session.commit()
            '''one_article = Article(
                article_id = p.article_id,
                title = p.title,
                createtime= p.createtime,
                modifytime = now_time,
                ownerid= p.ownerid,
                state = state
            ) '''
        else:
            one_article = Article(
                hostid=hostid,
                departmentid=departmentid,
                title = title,
                content = content,
                createtime=now_time,
                ownerid=ownerid,
                state=state
            ) 
            session.add(one_article)
            session.flush()
            article_id =one_article.article_id
            if(~hasrecordscore(flask_session.get('nl_user_id'),2,articleid=article_id)):
                session.add(new_scorerecord(flask_session.get('nl_user_id'),0,2,0,2,articleid=article_id))
            session.commit()
    return article_id  

#判断积分是否被加过，用来避免看文章或者答题重复积分
def hasrecordscore(userid,comefrom,readid=None,answerid=None,articleid=None):
    stmt = select(ScoreRecord).where(\
        ScoreRecord.userid == userid,\
            ScoreRecord.comefrom==comefrom,\
                ScoreRecord.readid==readid,\
                    ScoreRecord.answerid==readid,\
                        ScoreRecord.articleid==articleid)
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        if(len(result)==0):
            return False
        else:
            return True

#插入积分
def insert_scorerecord(userid,score1,score2,score3,comefrom,readid=None,answerid=None,articleid=None):
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with Session(engine) as session:
        one_record = ScoreRecord(
            userid = userid,
            score_1 =  score1,
            score_2 =  score2,
            score_3 =  score3,
            comefrom = comefrom,
            insertdate = now_time,
            readid=readid,
            answerid=answerid,
            articleid=articleid
        )
        session.add(one_record)
        session.commit()
    return True  


#new一个积分对象出来
def new_scorerecord(userid,score1,score2,score3,comefrom,readid=None,answerid=None,articleid=None):
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    one_record = ScoreRecord(
        userid = userid,
        score_1 =  score1,
        score_2 =  score2,
        score_3 =  score3,
        comefrom = comefrom,
        insertdate = now_time,
        readid=readid,
        answerid=answerid,
        articleid=articleid
    )
    return one_record


def user_hasread(userid,articleid):  #判断文章是否被阅读了
    stmt = select(ReadRecord).filter_by(userid=userid,articleid=articleid)
    with Session(engine) as session:
        result =  session.execute(stmt).scalars().all()
        if(len(result)!=0):
            return True
        return False
    
def paper_hasanswer(userid,paperid):  #判断试卷是否被回答了
    stmt = select(AnswerRecord).filter_by(userid=userid,paperid=paperid).filter(AnswerRecord.state != 2)
    with Session(engine) as session:
        result =  session.execute(stmt).scalars().all()
        if(len(result)!=0):
            return result[0].getmark
        return -1
    
def unlockpaper(answerid): #作废试卷，删除积分记录
    with Session(engine) as session:
        answerrecord = session.query(AnswerRecord).filter(AnswerRecord.recordid == answerid).update({'state':2})
        #stmt=update(answerrecord).values(state=2)
        session.query(ScoreRecord).where(ScoreRecord.answerid==answerid).delete()
       #session.execute(stmt)
        session.commit()

def deletefile(fileid): #删除文件
    with Session(engine) as session:
        file = session.query(File).filter_by(fileid=fileid).first()
        if (file is not None):
            session.delete(file)
            session.commit()
            return file
    return None


#插入文章对象
def insertfile(path,_type):
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with Session(engine) as session:
        one_file = File(
            path=path,
            insertdate=now_time,
            type=_type
        ) 
        session.add(one_file)
        session.flush()
        session.commit()
        return one_file.fileid

#更新文章 设置文章对应的文章id
def updatefile(fileid,articleid):
    with Session(engine) as session:
        stmt=update(File).where(File.fileid==fileid).values(articleid=articleid)
        session.execute(stmt)
        session.commit()

def alterpassword(userid,newpass):
    with Session(engine) as session:
        #user = session.query(User).where(User.userid==userid).first()
        #if user.password == oldpass:
        stmt=update(User).where(User.userid==userid).values(password=newpass)
        session.execute(stmt)
        session.commit()
        return True
            
        



    
'''
with Session(engine) as session:
    spongebob = Question(
        detail="今天晚上吃什么好？",
        type="1",
        Options=[Option(serial=0,detail="面包"),Option(serial=1,detail="粽子"),Option(serial=2,detail="粥"),Option(serial=3,detail="南瓜")],
    )   
    session.add_all([spongebob])
    session.commit()
'''