from flask import Flask
from flaskr import create_app
from flaskr import db
from flaskr.admin import model
from flask_script import Manager,commands
from flask_migrate import Migrate,MigrateCommand


app = create_app()

# from flaskr.admin import views
# from flaskr.home import vews



def create_db():
    db.create_all()

app.before_first_request(create_db)


manager = Manager(app)
migrate = Migrate(app,db)     # 扩展app   多个参数

manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    print("hello")


if __name__ == '__main__':
    manager.run()

