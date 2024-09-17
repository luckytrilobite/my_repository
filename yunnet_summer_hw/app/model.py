#規定資料庫的模型

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#連結資料庫
connect = "mysql+mysqlconnector://root:Hsbiteh@localhost:3306/yunnetsumdb"

#(我也不懂)
engine = create_engine(connect, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
dbsession = Session()

#規定資料庫的表格
class User(Base):
    __tablename__ = 'users'

    account = Column(String(20),primary_key=True)
    password = Column(String(20))
    mail = Column(String(30))
    phone = Column(String(14))

# user = session.query(User).filter_by(account = 'ABC').first()
# acc = "DEF"
# pasw = "456"
# ma = "DEF@mail.com"
# num = "0800-087-456"
# session.add(User(account=acc,password=pasw,mail=ma,phone=num))
# session.commit()