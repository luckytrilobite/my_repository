from flask import render_template,redirect,url_for,request,jsonify,session
from app import app
from app.funtion import checklogin,retunrndata,newacc

app.secret_key = '/Bite108'

@app.route("/")
def replace():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html",user = name)

#API
@app.route("/api/loginout",methods = ['POST'])
def loginout():
    info = request.get_json()

    if(info == None):
        return "no data",400
    
    account = info.get('account')

    if(info.get('logch') == 'login'):
        if(checklogin( account, info.get('password') )):
            session[account] = 'ok'
            return 'ok'
        else:
            return 'no'        
    else:
        session.pop('account', None)
        return 'ok'

@app.route("/api/getdata",methods = ['POST'])
def userdata():
    info = request.get_json()
    account = info.get('account')

    if ((session.get(account)) and (session[account] == 'ok')):
        data = retunrndata(account)
        return {'info': data,'statu':'ok'}
    else:
        return {'info': "",'statu':'no'}

@app.route("/api/signup",methods = ['POST'])
def signup():
    data = request.get_json()
    
    newacc(data)
    return 'ok'