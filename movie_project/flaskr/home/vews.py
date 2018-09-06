from . import home
from flaskr import db,create_app
from flask import current_app,url_for,render_template,request
from flaskr.admin import model
from flaskr.admin import form
from flaskr.admin.model import user,login_log,tag,movie,preview,comment,collection
from flaskr import db,create_app
from flask import current_app,url_for,render_template,request
import re
import hashlib


@home.route("/login",methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == "POST":
        usrdata = request.form.get("usr", None)
        print(usrdata)
        pwddata = request.form.get("pwd", None)
        pwddata_Md5 = hashlib.md5(pwddata.encode('utf8'))       #md5加密
        password_Md5 = pwddata_Md5.hexdigest()
        try:
            if '@'in usrdata:
                search_email = model.user.query.filter_by(email = usrdata).first()
                print(search_email)
                if search_email is not None and search_email.pwd == password_Md5:
                    return "登录成功"
                else:
                    return render_template("login.html",error ="用户名或者密码错误")
            elif re.match("^\d", usrdata):          #判断首字符是数字
                search_phone = model.user.query.filter_by(phone = usrdata).first()
                if search_phone is not None and search_phone.pwd == password_Md5:
                    return "登录成功"
                else:
                    return render_template("login.html",error ="用户名或者密码错误")
            else:
                search_username = model.user.query.filter_by(username = usrdata).first()
                print(search_username)
                if search_username is not None and search_username.pwd == password_Md5:
                    return "登录成功"
                else:
                    return render_template("login.html",error ="用户名或者密码错误")
        except Exception:
            return render_template("login.html",error ="用户名或者密码错误")


    return render_template("login.html")


@home.route("/register", methods=["GET", "POST"])
def register():
    register_form = form.RegisterForm()
    # print(register_form)
    if register_form.validate_on_submit():
        username = request.form.get("username",None)
        pwd = request.form.get("pwd",None)
        name = request.form.get("name",None)
        email = request.form.get("email",None)
        phone = request.form.get("phone",None)
        pwdagain = request.form.get("pwdagain",None)

        pwd_Md5 = hashlib.md5(pwd.encode('utf8'))       #md5加密
        password = pwd_Md5.hexdigest()
        print(password)
        user1 = model.user(username=username, pwd=password, name=name, email=email, phone=phone)

        db.session.add(user1)
        db.session.commit()

        return render_template("login.html")

    return render_template("register.html",rForm = register_form)



@home.route("/index")
def index():

    return render_template("index.html")


@home.route("/animation")
def animation():

    return render_template("animation.html")


@home.route("/playvideo")
def palyvideo():

    return render_template("playvideo.html")


@home.route("/user")
def user():
    return render_template("user.html")