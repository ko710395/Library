from flask import Flask,render_template,flash,redirect,url_for,Blueprint
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import sys

'''defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)'''

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SSLN'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'blog.login'
login_manager.init_app(app)
# db.drop_all()
@login_manager.user_loader
def load_user(user_id):
    from database import Users
    return Users.query.get(str(user_id))

def init():
    from view import blog
    app.register_blueprint(blueprint = blog)

if __name__ == '__main__':
    init()
    app.run(host="0.0.0.0",port=8000,debug=True)