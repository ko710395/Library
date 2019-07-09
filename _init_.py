from flask import Flask,render_template,Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MyFlaskApplication!' # 当要使用Session或Cookies的时候需要这个配置，后面随便设置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/[MySQL db name]" # 连接SQL的URI，后面自行填写相关SQL信息
app.config['JSON_AS_ASCII'] = False # 不转换为ASCII码输出，而是保留Unicode编码原样输出

db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'blog.login'
login_manager.init_app(app)

csrf = CsrfProtect()

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