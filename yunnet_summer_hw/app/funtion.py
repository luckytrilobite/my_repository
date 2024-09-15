from app.model import User,dbsession

def checklogin(acc,pasw):
    search = dbsession.query(User).filter_by(account = acc).first()
    if((search != None) and (pasw == search.password)):
        return True
    else:
        return False

def retunrndata(user):
    search = dbsession.query(User).filter_by(account = user).first()
    data = {
        "user":search.account,
        "mail":search.mail,
        "number":search.phone
        }
    return data

def newacc(new):
    dbsession.add(User(
        account=new['account'],
        password=new['password'],
        mail=new['mail'],
        phone=new['number']
    ))
    dbsession.commit()
    return
