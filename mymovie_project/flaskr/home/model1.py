from flaskr import db
import datetime

##################定义权限数据模型
class Auth(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(600), nullable=False)
    addtime = db.Column(db.DateTime,nullable=False,index=True,default=datetime.datetime.now())


##################角色模型
class Role(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    auths = db.Column(db.String(300), nullable=False)
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.datetime.now())


###############管理员
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    pwd = db.Column(db.String(200), nullable=False)
    is_super = db.Column(db.SmallInteger, nullable=False)
    Adminlogs = db.relationship("Adminlog", backref='Admin', lazy="dynamic")
    Oplogs = db.relationship("Oplog", backref='Admin', lazy="dynamic")


#################登录日志
class Adminlog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    Admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100), nullable=False)
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.datetime.now())


################操作日志
class Oplog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    Admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(200), nullable=False)
    Oplog = db.Column(db.String(200), nullable=False)
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.datetime.now())





