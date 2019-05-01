from database import Users
from _init_ import login_manager,db,app
import json,os
from werkzeug.utils import secure_filename
from methods import Login,Search
from flask import Blueprint
from flask_login import login_required

blog = Blueprint('blog',__name__)

dire = os.path.abspath(os.path.dirname(__file__))

login_manager.login_view = "/login/"

login_manager.login_message = "Please Login First!"

@blog.route("/",methods=['GET','POST'])
def index():
    return Login.index()

@blog.route("/login/",methods=['GET','POST'])
def login():
    return Login.login()

@blog.route("/register/",methods=['GET','POST'])
def register():
    return Login.register()

@blog.route("/logout/",methods=['GET','POST'])
@login_required
def logout():
    return Login.logout()

@blog.route("/search/",methods=['GET','POST'])
def search():
    return Search.search()

@blog.route("/reading/",methods=['POST'])
def reading():
    return Search.reading()

@blog.route("/like/",methods=['GET','POST'])
@login_required
def like():
    return Search.like()

@blog.route("/if_in_like/",methods=['POST'])
@login_required
def if_in_like():
    return Search.if_in_like()

@blog.route("/nolike/",methods=['POST'])
@login_required
def nolike():
    return Search.nolike()

@blog.route("/what_like/",methods=['POST'])
@login_required
def what_like():
    return Search.what_like()