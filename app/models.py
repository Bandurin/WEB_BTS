# -*- coding: utf-8 -*-

from app import db
from datetime import datetime
import hashlib
from flask_login import UserMixin
from app import login


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name  = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)


    def set_password(self,passwd):
        self.password = hashlib.md5(passwd.encode('utf-8')).hexdigest()

    def check_password(self,passwd):
        if hashlib.md5(passwd.encode('utf-8')).hexdigest() == self.password:
            return True
        else:
            return False


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
