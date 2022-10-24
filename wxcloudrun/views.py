from flask import render_template, request
from run import app

@app.route('/')

def login():
    user_wx_openid=request.headers.get('x-wx-openid')
    
    return render_template('login.html',openid=user_wx_openid)

@app.route("/MP_verify_PertlLt3DIqUIQJv.txt")

def verify():
    return "PertlLt3DIqUIQJv"