from .import admin
import hashlib
from . import model,form

from flaskr.home import model1

from flaskr.admin.model import user,login_log,tag,movie,preview,comment,collection
from flaskr import db,create_app
from flask import current_app,url_for,render_template,request,redirect
import re
import hashlib
import json

#User-Agent	Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/61.0

# -*- coding:utf_8 -*-
import requests
def douban():
    header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:61.0) Gecko/20100101 Firefox/61.0"}
    weather = requests.get("https://movie.douban.com/trailers",headers = header)

    weather.encoding="utf8"
    # print(weather.text)
    return weather.text



@admin.route("/test")
def test():
    # print("12345")
    # return "home"
    return render_template("test.html")


@admin.route("/newbase1")
def base():
    # print("12345")
    # return "home"
    return render_template("newbase1.html")

@admin.route("/auth_add",methods=["GET", "POST"])
def auth_add():
    if request.method == "POST":
        name = request.form.get("name", None)
        print(name)
        url = request.form.get("url", None)
        print(url)
        auth = model1.Auth(name=name, url=url)
        db.session.add(auth)
        db.session.commit()
    return render_template("auth_add.html")


@admin.route("/auth_list")
def auth_list():
    auth = model1.Auth.query.all()
    return render_template("auth_list.html",auth=auth)


@admin.route("/comment_list")
def comment_list():
    # print("12345")
    # return "home"
    return render_template("comment_list.html")


@admin.route("/movie_list")
def movie_list():
    # print("12345")
    # return "home"
    movie = model.movie.query.all()
    return render_template("movie_list.html",movie=movie)



@admin.route("/movie_add",methods=["GET", "POST"])
def movie_add():
    tags = model.tag.query.all()
    if request.method == "POST":
        title = request.form.get("title", None)
        url = request.form.get("url", None)
        info = request.form.get("info", None)
        logo = request.form.get("logo", None)
        star = request.form.get("star", None)
        playnum = request.form.get("playnum", None)
        commentnum = request.form.get("commentnum", None)
        newtag = request.form.get("tags", None)
        area = request.form.get("area", None)
        length = request.form.get("length", None)
        release_time = request.form.get("release_time", None)
        print(request.form)
        movie = model.movie(title=title, url=url, info=info,logo=logo,playnum=playnum,newtag=newtag,commentnum=commentnum,star=star,area=area,length=length,release_time=release_time)
        db.session.add(movie)
        db.session.commit()
    return render_template("movie_add.html",tags=tags)



@admin.route("/admin_list")
def admin_list():
    admin = model1.Admin.query.all()
    return render_template("admin_list.html", admin=admin)


@admin.route("/admin_add",methods=["GET", "POST"])
def admin_add():
    if request.method == "POST":
        name = request.form.get("adminname", None)
        # print(name)
        pwd = request.form.get("adminpwd", None)
        # print(pwd)
        pwdagain = request.form.get("pwdagain",None)
        # print(pwdagain)
        is_super = request.form.get("adminrole",None)
        # print(is_super)

        pwd_Md5 = hashlib.md5(pwd.encode('utf8'))       #md5加密
        password_Md5 = pwd_Md5.hexdigest()
        admin = model1.Admin(name=name, pwd=password_Md5,is_super=is_super)
        db.session.add(admin)
        db.session.commit()
    return render_template("admin_add.html")


@admin.route("/role_add",methods=["GET", "POST"])
def role_add():
    auth = model1.Auth.query.all()
    if request.method == "POST":
        name = request.form.get("name", None)
        auths = request.form.getlist("input_url",None)

        str = ""
        for i in auths:
            str = str +"/"+i
        print(str)
            # print(auths)
        role = model1.Role(name=name,auths=str)
        db.session.add(role)
        db.session.commit()

    return render_template("role_add.html", auth=auth)

@admin.route("/role_list")
def role_list():
    role = model1.Role.query.all()
    return render_template("role_list.html" ,role=role)

@admin.route("/tag_add",methods=["GET", "POST"])
def tag_add():
    if request.method == "POST":
        name = request.form.get("name",None)

        tag = model.tag(tagName=name)
        db.session.add(tag)
        db.session.commit()

    # role = model1.Role.query.all()
    return render_template("tag_add.html" )

@admin.route("/tag_list",methods=["POST","GET"])
def tag_list():
    tag = model.tag.query.all()

    if request.method == "POST":
        op = request.form.get('op')
        print("打印op is ????\n", op)
        if op == "del_tag":
            id = request.form.get("id", None)
            try:
                deltag = model.tag.query.filter_by(id=id).first()
                db.session.delete(deltag)
                db.session.commit()
            except Exception as e:
                print("打印删除标签的时候出现的错误", e)
                return "error"
        elif op == "edit_tag":
            formdata = request.form.get("formdata", None)
            formobj = json.loads(formdata)
            print("打印formObj\n", formobj)
            tagid = request.form.get("id", None)
            print("打印 id", tagid)
            tagName = formobj['tagName']
            addtime = formobj['addTime']
            try:
                edit_tag = model.tag.query.filter_by(id=tagid).first()
                print("edit_tag\n", edit_tag)
                edit_tag.tagName = tagName
                edit_tag.addTime = addtime
                db.session.commit()
            except Exception as e:
                print("打印编辑标签的时候出现的错误", e)
                return "error"
        return "ok"
    return render_template("tag_list.html" ,tag=tag)


@admin.route("/userloginlog_list")
def userloginlog_list():

    return render_template("userloginlog_list.html")




userview = []
@admin.route("/user_list",methods=["GET", "POST"])
def user_list():
    user = model.user.query.all()
    if request.method == "POST":
        name = request.form.get('name', None)
        # print("1234567")
        # print(name)
        userview.append(name)
        return redirect("/user_view",userview=userview)
    return render_template("user_list.html",user=user)


@admin.route("/user_view",methods=["GET", "POST"])
def user_view():
    global userview
    print(userview)
    view = model.user.query.filter_by(id=userview[0]).first()
    userview=[]
    return render_template("user_view.html",view=view)



from bs4 import BeautifulSoup
@admin.route("/preview_add",methods=["GET","POST"])
def preview_add():
    soup = BeautifulSoup(douban(), features="lxml")
    r = soup.select("li img")
    for item in r:
        title1 = item.attrs.get("alt", None)
        logo1 = item.attrs.get("src", None)
        name = model.preview.query.filter_by(title=title1).all()
        # print(name)
        num = 0
        if name:
            for i in name:
                if i.title == title1:
                    # print(23456)
                    if i.logo == logo1:
                        num = num+1
                        # preview = model.preview(title=title1, logo=logo1)
                        # db.session.add(preview)
                        # db.session.commit()
                        print("预告已存在")
                        break
            if num == 0:
                preview = model.preview(title=title1, logo=logo1)
                db.session.add(preview)
                db.session.commit()
                print("成功")
        else:
            preview = model.preview(title=title1, logo=logo1)
            db.session.add(preview)
            db.session.commit()
        # try:
        #     if title1 == model.preview.query.filter_by(title=title1).title:
        #         if logo == model.preview.query.filter_by(title=title1).logo:
        #             print("预告已存在")
        #     else:
        #         print("成功")
        #         preview = model.preview(title=title1, logo=logo)
        #         db.session.add(preview)
        #         db.session.commit()
        # except Exception:
        #     print("预告已存在")
        #

        # print(title)  # -----属性里面的class
        # print(logo)  # -----属性里面的class
        # preview = model.preview(title=title1, logo=logo1)
        # db.session.add(preview)
        # db.session.commit()

    if request.method == "POST":
        title=request.form.get("title",None)
        logo=request.form.get("logo",None)
        preview = model.preview(title=title,logo=logo)
        db.session.add(preview)
        db.session.commit()
    return render_template("preview_add.html")

@admin.route("/preview_list")
def preview_list():
    preview = model.preview.query.all()
    # print(preview)
    return render_template("preview_list.html",preview=preview)

@admin.route("/oplog_list")
def oplog_list():
    # tag = model.tag.query.all()
    return render_template("oplog_list.html")

@admin.route("/moviecollect_list")
def moviecollect_list():
    # tag = model.tag.query.all()
    return render_template("moviecollect_list.html")

@admin.route("/adminloginlog_list")
def adminloginlog_list():
    # tag = model.tag.query.all()
    return render_template("adminloginlog_list.html")

