from datetime import datetime
from sqlalchemy import create_engine,CHAR, TEXT, VARCHAR, Column,ForeignKey,Integer,select,DateTime ,update
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from flask import session as flask_session
from sqlalchemy.orm import Bundle,aliased
from sqlalchemy.sql import func
import config
Base = declarative_base()

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

engine = create_engine(config.DB_URI)

Base.metadata.create_all(engine)

def get_alluser():    
    with Session(engine) as session:
        stmt = select(User)
        result =  session.execute(stmt)
        return result.scalars().all()


def get_user_byid(id):    
    with Session(engine) as session:
        stmt = select(User).where(User.userid==id)
        result =  session.execute(stmt)
        login_user = result.first()
        return login_user

def get_user_byloginname(loginname):    
    with Session(engine) as session:
        stmt = select(User).where(User.workid==loginname)
        result =  session.execute(stmt)
        login_user = result.first()
        return login_user

def get_all_paper():             
    stmt = select(Paper)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()
    
def get_all_paper_filterbystate(statelist):             
    stmt = select(Paper).where(Paper.state.in_(statelist))
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()
    
def get_all_paper_filterbystate_user(statelist,ownerid):             
    stmt = select(Paper).where(Paper.state.in_(statelist),Paper.ownerid==ownerid)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()

def get_paper_byid(paper_id):
    stmt = select(Paper).where(Paper.paperid == paper_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()

def get_paper_questions_byid(paper_id):
    stmt = select(Question).where(Question.paperid == paper_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.scalars().all()

def delete_paper(paper_id):
    with Session(engine) as session:
        paper = session.query(Paper).filter_by(paperid=paper_id).first()
        if (paper is not None):
            session.delete(paper)
            session.commit()
            return paper
    return None

def drop_paper(paper_id):
    with Session(engine) as session:
        stmt=update(Paper).where(Paper.paperid==paper_id).values(state=2)
        session.execute(stmt)
        paper = session.query(Paper).filter_by(paperid=paper_id).first()
        return paper

def delete_question_bypaperid(paper_id):
    with Session(engine) as session:
        Questions = session.query(Question).filter_by(paperid=paper_id)
        if (Questions is not None):
            for q in Questions:
                session.delete(q)
            session.commit()


def insert_question(paper_id,type,detail,mark):
    with Session(engine) as session:
        one_question = Question(
                paperid = paper_id,
                type=type,
                detail=detail,
                mark=mark
        ) 
        session.add_all([one_question])
        session.commit()

def insert_paper(_paper_title,paper_id,count,paper_state,_ownerid,_questions,hostid,departmentid):
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

def drop_answerrecord(paper_id:int,user_id:int):
    with Session(engine) as session:
        stmt=update(AnswerRecord).where(AnswerRecord.paperid==paper_id,AnswerRecord.userid==user_id).values(state=2)
        session.execute(stmt)
        #record = session.query(AnswerRecord).filter_by(paperid=int(paper_id),userid=user_id).filter(AnswerRecord.state!=2).first()
        session.commit()
        return True



def insert_record(paper_id,user_id,state,getmark):
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


def insert_readrecord(article_id,user_id):
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


def get_role_byuser(current_user):
    role_id=2                      #默认为匿名用的id
    if(current_user is not None):
        role_id = current_user.roleid
    with Session(engine) as session:
        role = session.query(Role).filter_by(roleid=role_id).first()
        return role

def get_user_bysession():
    with Session(engine) as session:
        u = session.query(User).filter_by(userid=flask_session.get('nl_user_id')).first()
        return u

def get_user_scores(id):
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(func.sum(ScoreRecord.score_1).label("score1"),func.sum(ScoreRecord.score_2).label("score2"),func.sum(ScoreRecord.score_3).label("score3")).filter_by(userid=id)
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result

def get_user_answerrecord(id):
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(AnswerRecord,ScoreRecord).filter_by(userid=id).filter(AnswerRecord.state != 2)\
        .outerjoin(ScoreRecord)\
        .order_by(AnswerRecord.insertdate.desc())
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result

def get_answerrecord_bypaper(id):
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(AnswerRecord,User).filter_by(paperid=id).filter(AnswerRecord.state != 2)\
        .outerjoin(User)\
        .order_by(AnswerRecord.insertdate.desc())
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result
    
def get_user_readrecord(id):
    #stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(ReadRecord,ScoreRecord).filter_by(userid=id)\
        .outerjoin(ScoreRecord)\
        .order_by(ReadRecord.insertdate.desc())
    with Session(engine) as session:
        result =  session.execute(stmt).all()
        return result
    
def get_all_readrecord():
#stmt = select(AnswerRecord.userid,func.sum(AnswerRecord.score).label("scores")).group_by(AnswerRecord.userid)
    stmt = select(ReadRecord)
    with Session(engine) as session:
        result =  session.execute(stmt).scalars().all()
        return result


def delete_article(article_id):
    with Session(engine) as session:
        article = session.query(Article).filter_by(article_id=article_id).first()
        if (article is not None):
            session.delete(article)
            session.commit()
            return article
    return None

def drop_article(article_id):
    with Session(engine) as session:
        with Session(engine) as session:
            stmt=update(Article).where(Article.article_id==article_id).values(state=2)
            session.execute(stmt)
            article = session.query(Article).filter_by(article_id=article_id).first()
            return article


def insert_article(article_id,title,content,ownerid,state,hostid,departmentid):
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

def get_all_article():    
    stmt = select(Article,func.count(ReadRecord.readid)).outerjoin(ReadRecord).group_by(Article.article_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.all()
    
def get_all_article_filterbystate():    
    stmt = select(Article,func.count(ReadRecord.readid)).outerjoin(ReadRecord).where(Article.state==1).group_by(Article.article_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.all()
    

def get_all_article_filterbystate_user(ownerid):    
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
def get_article_byid(article_id):
    stmt = select(Article,func.count(ReadRecord.readid)).outerjoin(ReadRecord).where(Article.article_id == article_id)
    with Session(engine) as session:
        result =  session.execute(stmt)
        return result.all()


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


def get_alldepartment():
    with Session(engine) as session:
        stmt = select(Department)
        result =  session.execute(stmt)
        return result.scalars().all()
    

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