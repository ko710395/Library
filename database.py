from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required,current_user
from _init_ import db,login_manager


class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(30), primary_key = True)
    pwd = db.Column(db.String(20))
    is_authenticated = True
    is_active = True
    is_anonymous = False

    def __init__(self,id,pwd):
        self.id = id
        self.pwd = pwd

    def __repr__(self):
        return '<Users %r>' % self.id

    def get_id(self):
        return self.id

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.String(20), primary_key = True)
    Name = db.Column(db.String(30))
    Author = db.Column(db.String(30))
    PublishingHouse = db.Column(db.String(30))
    Category = db.Column(db.String(30))

    def __init__(self,id,Name,Author,PublishingHouse,Category):
        self.id = id
        self.Name = Name
        self.Author = Author
        self.PublishingHouse = PublishingHouse
        self.Category = Category


class Relationship(db.Model):
    __tablename__ = 'relationship'
    id = db.Column(db.String(30), primary_key = True)
    books = db.Column(db.String(500))

    def __init__(self,id,books):
        self.id = id
        self.books = books