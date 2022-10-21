from flask import render_template, request
from run import app

@app.before_request
def before_request():
    ip = request.remote_addr
    url = request.url
    print(ip)
    print(url)

@app.route('/')

def login():
    user_wx_openid=request.headers.get('x-wx-openid')
    print(user_wx_openid)
    return render_template('login.html')

