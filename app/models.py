import email
from enum import unique
from turtle import title
from xmlrpc.client import DateTime
from  . import db


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_path = db.Column(db.String(20), unique=True, nullable=False, default='default.jpg')
    password =  db.Column(db.String(20), nullable=False)
    posts = db.relashionship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f"User('{self.username}' '{self.email}', '{self.image_path}')"


class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=DateTime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Comment('{self.title}', '{self.date_posted})"