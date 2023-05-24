#数据库配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'learningsys'
USERNAME = 'root'
PASSWORD = 'A123456a'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

#session密码
SECRET_KEY = 'Xiao!Duan@Tui#Pao$De%Kuai.'