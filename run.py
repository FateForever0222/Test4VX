# 创建应用实例
import sys

from flask import Flask, render_template, request, redirect, url_for, flash, session


from wxcloudrun import app


@app.route('/')
def login():
    return render_template('login.html')
# 启动Flask Web服务
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2])
