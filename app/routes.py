# -*- coding: utf-8 -*-

from app import app
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.forms import LoginForm
from app.models import User
from datetime import datetime
from flask import jsonify
import netifaces as ni
import random
from connect import GoBts

@app.route('/')
@app.route('/index')
@login_required
def index():


    ni.ifaddresses('wlan0')
    IP = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    sensor = {'sen1':IP}

    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]

    return render_template('index.html',title = 'HOME', sensor = sensor, posts = posts, user = user)


@app.route('/goForward', methods=['POST'])
@login_required
def goForward():
    var = [1,110,0]
    bts = GoBts()
    bts.writeNumber(var)
    #time= jsonify({'text': str(datetime.now())})
    return 'GO'

@app.route('/goBackward', methods=['POST'])
@login_required
def goBackward():
    var = [2,110,0]
    bts = GoBts()
    bts.writeNumber(var)
    #time= jsonify({'text': str(datetime.now())})
    return 'GO'

@app.route('/goLeft', methods=['POST'])
@login_required
def goLeft():
    var = [3,150,0]
    bts = GoBts()
    bts.writeNumber(var)
    #time= jsonify({'text': str(datetime.now())})
    return 'GO'

@app.route('/goRight', methods=['POST'])
@login_required
def goRight():
    var = [4,150,0]
    bts = GoBts()
    bts.writeNumber(var)
    #time= jsonify({'text': str(datetime.now())})
    return 'GO'


@app.route('/stop', methods=['POST'])
@login_required
def stop():
    var = [0,0,0]
    bts = GoBts()
    bts.writeNumber(var)
   # time= jsonify({'text': str(datetime.now())})
    return 'STOP'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sing In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
