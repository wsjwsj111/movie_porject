from .import admin

from . import model,form

from flaskr.home import model1

from flaskr.admin.model import user,login_log,tag,movie,preview,comment,collection
from flaskr import db,create_app
from flask import current_app,url_for,render_template,request
import re
import hashlib




@admin.route("/newbase")
def newbase():
    # print("12345")
    # return "home"
    return render_template("newbase.html")

