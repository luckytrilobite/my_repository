# 後段的主要處理函數

# import 資料庫
from app.model import User,dbsession

def checklogin(acc,pasw):
    # 搜尋資料庫的密碼
    search = dbsession.query(User).filter_by(account = acc).first()
    #檢測密碼
    if((search != None) and (pasw == search.password)):
        return True
    else:
        return False

def retunrndata(user):
    #搜尋資料庫的用戶資料
    search = dbsession.query(User).filter_by(account = user).first()
    #打包成data字典
    data = {
        "user":search.account,
        "mail":search.mail,
        "number":search.phone
        }
    return data

def newacc(new):
    #將輸入(new)資料創建為資料庫內容
    dbsession.add(User(
        account=new['account'],
        password=new['password'],
        mail=new['mail'],
        phone=new['number']
    ))
    #儲存資料
    dbsession.commit()
    return
