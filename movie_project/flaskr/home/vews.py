from . import home
from flaskr import db,create_app
from flask import current_app,url_for,render_template,request


@home.route("/newbase")
def newbase():
    # print("12345")
    # return "home"
    return render_template("newbase.html")


@home.route("/index")
def index():
    # print("12345")
    # return "home"
    return render_template("index.html")


@home.route("/animation")
def animation():
    # print("12345")
    # return "home"
    return render_template("animation.html")


