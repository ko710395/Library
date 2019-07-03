from flask import Flask,render_template,Blueprint,jsonify,request,Request
from database import Users,Books,Relationship
from flask_login import login_manager,login_user,UserMixin,logout_user,login_required,current_user
from _init_ import login_manager,db,app,csrf
import json,os,re
from sqlalchemy import and_

class Login():
    def index(): # 首页，因为没在Nginx上部署所以第一次访问时先return一个html，之后就不会这样用了
        return render_template("index.html")


    def pwd(str): # 用于检测密码是否符合标准，复杂度同苹果账号，即必须同时存在大小写字母+数字+特殊符号，以及不能连续三个相同字符
        result = re.search(r"^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$", str)
        if result:
            result = re.search(r"(.)\1{2}",str)
            if not result:
                return "true"
            else:
                return "密码不能包含连续三个相同的字符"
        else:
            return "密码需要同时包含大小写字母、数字以及特殊符号"


    def login(): # 登录
        if request.method == 'POST':
            data = json.loads(request.get_data().decode('utf-8'))
            db.session.commit() #查询前的commit都用于另起事务防止结果重复读，下同
            user = Users.query.filter(Users.id == data['name']).first()
            if user is not None and user.pwd == data['pwd']:
                login_user(user)
                return jsonify(
                    success = True,
                    data = "Login Successfully!"
                )
            else:
                return jsonify(
                    success = True,
                    data = "Account or pwd Error!"
                )
        else:
            return render_template("login.html")


    def register(): # 注册
        if request.method == 'POST':
            data = json.loads(request.get_data().decode('utf-8'))
            res = Login.pwd(data['pwd'])
            if res != "true":
                return jsonify(
                    success = True,
                    data = res
                )
            else:
                db.session.commit()
                user = Users.query.filter(Users.id == data['name']).first()
                if user is None:
                    user = Users(id = data['name'],pwd = data['pwd'])
                    db.session.add(user)
                    db.session.commit()
                    user = Relationship(id = data['name'],books = '')
                    db.session.add(user)
                    db.session.commit()
                    return jsonify(
                        success = True,
                        data = "Register Successfully!"
                    )
                else:
                    return jsonify(
                        success = True,
                        data = "This Account has been Existed!"
                    )
        else:
            return render_template("register.html")


    def logout(): # 登出
        logout_user()
        return jsonify(
            success = True,
            data = "Logout Successfully!"
        )
    


class Search():
    def search():   # *************************************** 这个需要进一步优化，但是优化方案暂时想不到
        if request.method == 'POST':
            data = request.get_data().decode('utf-8')
            data = json.loads(data)
            str_data1 = "%" #书名
            str_data2 = "%" #作者
            str_data3 = "%" #出版社
            str_data4 = []  #分类
            if (data['name']):
                str_data1 = str_data1 + data['name'] + "%"
            if (data['author']):
                str_data2 = str_data2 + data['author'] + "%"
            if (data['publishinghouse']):
                str_data3 = str_data3 + data['publishinghouse'] + "%"
            if (data['category']):
                for x in data['category']:
                    x = "%" + x + "%"
                    str_data4.append(x)
            print(str_data4)
            k = and_(*[Books.Category.like(x) for x in str_data4])
            print(k)
            db.session.commit()
            data = Books.query.filter(Books.Name.like(str_data1), 
                                      Books.Author.like(str_data2), 
                                      Books.PublishingHouse.like(str_data3),
                                      k).all()
            li = []
            for k in data:
                li.append({'Name' : k.Name,
                            'Author' : k.Author,
                            'PublishingHouse' : k.PublishingHouse,
                            'Category' : k.Category,
                            'id' : k.id})
            return jsonify(
                success = True,
                data = li
            )
        else:
            return render_template("search.html")

    def reading(): # 阅读，即打开文本，每本书都有个数字id并且后台以此id命名对应txt电子书
        if request.method == 'POST':
            id = request.get_data().decode('utf-8')
            id = json.loads(id)
            with open("./books/" + id['id'] + ".txt") as book:
                data = ''.join(book.readlines())
                return jsonify(
                    success = True,
                    data = data
                )
        else:
            return jsonify(
                success = False,
                data = "Incorrect Access!"
            )

            

    def like():
        if request.method == 'POST':
            data = json.loads(request.get_data().decode('utf-8'))
            db.session.commit()
            rela = Relationship.query.filter(Relationship.id == current_user.id).first()
            rela.books = rela.books + " " + data['bookid']
            db.session.commit()
            return jsonify(
                success = True,
                data = '添加成功！'
            )
        else:
            return Search.what_like()

    def if_in_like():
        if request.method == 'POST':
            data = json.loads(request.get_data().decode('utf-8'))
            db.session.commit()
            rela = db.session.query(Relationship).filter(Relationship.id == current_user.id,
                                                        Relationship.books.like("%" + data['id'] + "%")).all()
            # if rela:
            #     return jsonify(
            #         data = True
            #     )
            # else:
            #     return jsonify(
            #         data = False
            #     )
            return jsonify(
                data = bool(rela)
            )
        
        else:
            return jsonify(
                success = False,
                data = "Incorrect Access!"
            )


    def nolike():
        if request.method == 'POST':
            data = json.loads(request.get_data().decode('utf-8'))
            db.session.commit()
            rela = Relationship.query.filter(Relationship.id == current_user.id).first()
            rela.books = rela.books.replace(" " + data['bookid'],"")
            Relationship.query.all()
            return jsonify(
                success = True,
                data = '删除成功！'
            )
        
        else:
            return jsonify(
                success = False,
                data = "Incorrect Access!"
            )

    def what_like():
        li = []
        db.session.commit()
        res = Relationship.query.filter(Relationship.id == current_user.id).first()
        x = 1
        while x < len(res.books)-3:
            li.append(res.books[x:x+4])
            x = x + 5
        print(li)
        li2 = []
        for y in li:
            db.session.commit()
            res = Books.query.filter(Books.id == y).first()
            li2.append({'Name' : res.Name,
                        'Author' : res.Author,
                        'PublishingHouse' : res.PublishingHouse,
                        'Category' : res.Category,
                        'id' : res.id})
        return jsonify(
            success = True,
            data = li2
        )