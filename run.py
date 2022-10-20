# 创建应用实例
import sys

from django.shortcuts import render, render_to_response

from wxcloudrun import app


@app.route('/login')
def login():
    return render_to_response('login.html')
# 启动Flask Web服务
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2])
