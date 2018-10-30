from flask import request, redirect, url_for, render_template, flash
from flaskr import app

@app.route('/')
def index():
    print ('run')
    return render_template('index.html')
