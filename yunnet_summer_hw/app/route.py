#設定路由

from flask import render_template,redirect,url_for,request,jsonify,session
from app import app
from app.funtion import checklogin,retunrndata,newacc

#加密session的密碼?
app.secret_key = '/Bite108'

#跟路由
@app.route("/")
def replace():
    #重新導向到/home
    return redirect(url_for('home'))

@app.route("/home")
def home():
    # 回傳登入、註冊的html
    return render_template("index.html")

@app.route("/profile/<name>")
#       根據不同使用者^  改變不同內容
def profile(name):
    # 回傳profile html把user傳進去
    return render_template("profile.html",user = name)

#API

# 登入登出api
@app.route("/api/loginout",methods = ['POST'])
def loginout():
    #獲取請求資訊
    info = request.get_json()
    #沒有東西就回傳錯誤
    if(info == None):
        return "no data",400
    
    #把帳號資料拿出來比對
    account = info.get('account')
    if(info.get('logch') == 'login'): #如果是登入
        if(checklogin( account, info.get('password') )):
            #用session儲存登入沒
            session[account] = 'ok'
            return 'ok'
        else:
            return 'no'        
    else:
        #登出要把session處理掉
        session.pop('account', None)
        return 'ok'

# 獲取使用者資料
@app.route("/api/getdata",methods = ['POST'])
def userdata():
    info = request.get_json()
    account = info.get('account')
    # 把使用者資料拿出來return回前端
    if ((session.get(account)) and (session[account] == 'ok')):
        data = retunrndata(account)
        return {'info': data,'statu':'ok'}
    else:
        return {'info': "",'statu':'no'}

# 跟據新增帳號的資料調去新建帳號函數
@app.route("/api/signup",methods = ['POST'])
def signup():
    data = request.get_json()
    
    newacc(data)
    return 'ok'