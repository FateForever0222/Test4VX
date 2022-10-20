from flask import render_template, request
from run import app


@app.route('/')

def login():
    return render_template('login.html')

