from flask import Flask,render_template,flash,Blueprint,redirect,url_for,jsonify,request,Request
from database import Users,Books,Relationship
from flask_login import login_manager,login_user,UserMixin,logout_user,login_required,confirm_login,current_user
from _init_ import login_manager,db,app
import json,os,re
from sqlalchemy import and_

class Login():
    def index():
        return render_template("index.html")


    def pwd(str):
        result = re.search(r"^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$", str)
        if result:
            result = re.search(r"(.)\1{2}",str)
            if not result:
                return "true"
            else:
                return "密码不能包含连续三个相同的字符"
        else:
            return "密码需要同时包含大小写字母、数字以及特殊符号"


    def login():
        if request.method == 'POST':
            data = request.get_data().decode('utf-8')
            data = json.loads(data)
            db.session.commit()
            user = Users.query.filter(Users.id == data['name']).first()
            # str1 = "%"
            # user = Users.query.filter(Users.id.like(str1)).first()
            # print(str1)
            # print(user)
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


    def register():
        if request.method == 'POST':
            data = request.get_data().decode('utf-8')
            data = json.loads(data)
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


    def logout():
        logout_user()
        return jsonify(
            success = True,
            data = "Logout Successfully!"
        )
    


class Search():
    def search():
        if request.method == 'POST':
            data = request.get_data().decode('utf-8')
            data = json.loads(data)
            str_data1 = "%"
            str_data2 = "%"
            str_data3 = "%"
            str_data4 = []
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
            print(li)
            return jsonify(
                success = True,
                data = li
            )
        else:
            return render_template("search.html")

    def reading():
        if request.method == 'POST':
            id = request.get_data().decode('utf-8')
            id = json.loads(id)
            data = "./books/" + id['id'] + ".txt"
            book = open(data)
            res = book.readlines()
            data = ''.join(res)
            book.close()
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
            data = request.get_data().decode('utf-8')
            data = json.loads(data)
            print(current_user.id)
            print(data['bookid'])
            db.session.commit()
            rela = Relationship.query.filter(Relationship.id == current_user.id).first()
            rela.books = rela.books + " " + data['bookid']
            db.session.commit()
            Relationship.query.all()
            print(rela.books)
            return jsonify(
                success = True,
                data = '添加成功！'
            )

        else:
            return Search.what_like()

    def if_in_like():
        if request.method == 'POST':
            data = request.get_data().decode('utf-8')
            data = json.loads(data)
            db.session.commit()
            rela = db.session.query(Relationship).filter(Relationship.id == current_user.id,
                                                        Relationship.books.like("%" + data['id'] + "%")).all()
            print(rela)
            if rela:
                return jsonify(
                    data = True
                )
            else:
                return jsonify(
                    data = False
                )
        
        else:
            return jsonify(
                success = False,
                data = "Incorrect Access!"
            )


    def nolike():
        if request.method == 'POST':
            data = request.get_data().decode('utf-8')
            data = json.loads(data)
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