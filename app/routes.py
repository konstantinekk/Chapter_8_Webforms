from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/Home')
def index ():
    """Home URL"""
    return render_template('index.html', title='Home Page')


@app.route('/About-me')
def about_me():
    """about Me URL"""
    return render_template('about_me.html', title='About Me Page')


@app.route('/Login', methods=['GET','POST']) 
def login():
    """Login URL"""
    form = LoginForm()    
    return render_template('Login_form.html', title='Login', form=form)
