from flask import request, redirect, url_for, render_template, flash
from flaskr import app

@app.route('/')
def show_entries():
    return render_template('layout.html')
