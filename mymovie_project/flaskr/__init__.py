from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile("config.py",silent=True)

    from flaskr.admin import admin as admin_blueprint
    from flaskr.home import home as home_blueprint

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(home_blueprint)


    db.init_app(app)
    return app