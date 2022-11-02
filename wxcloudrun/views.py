from time import time
from flask import render_template, request
from run import app
import requests
@app.route('/login')

def login():
    user_wx_openid=request.headers.get('x-wx-openid')
    return user_wx_openid

# def demo():
#     return render_template('demo.html')

@app.route("/MP_verify_PertlLt3DIqUIQJv.txt")

# def verify():
#     return "PertlLt3DIqUIQJv"

# @app.route("/getOpenid")
# def getOpenid():

#     url_base = request.args.get("url")
#     secret=request.args.get("secret")
#     code=request.args.get("code")
#     grant_type=request.args.get("grant_type")
#     url=url_base+"&secret="+secret+"&code="+code+"&grant_type="+grant_type
#     req=requests.get(url[1:-1],timeout=30)
#     # print(req)
#     res=req.json()['openid']
#     # print(res)
#     return render_template('openid.html',url2=res)

