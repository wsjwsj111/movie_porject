from flaskr import db
import uuid
import datetime

def gen_id():
    return uuid.uuid4().hex

################会员
class user(db.Model):
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    username = db.Column(db.String(300),nullable=False)
    pwd = db.Column(db.String(300),nullable=False)
    name = db.Column(db.String(400),nullable=True)
    email = db.Column(db.String(300),nullable=False)
    phone = db.Column(db.String(300),nullable=False)
    info = db.Column(db.Text,nullable=True)
    face = db.Column(db.String(300),nullable=True)
    usertime = db.Column(db.DateTime,nullable=True,default=datetime.datetime.now())
    uuid = db.Column(db.String(300),nullable=True,default=gen_id)

    userid = db.relationship("login_log", backref='user', lazy="dynamic")
    comments = db.relationship("comment", backref='user', lazy="dynamic")
    collections = db.relationship("collection", backref='user', lazy="dynamic")



##############################会员登录日志

class login_log(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(200),nullable=False)
    logintime = db.Column(db.DateTime,nullable=False,default=datetime.datetime.now())






movie_tag = db.Table('movie_tag',
                     db.Column('tag_id', db.INTEGER, db.ForeignKey('tag.id', ondelete="SET NULL"), nullable=True),
                     db.Column('movie_id', db.INTEGER, db.ForeignKey('movie.id', ondelete="SET NULL"), nullable=True)
                     )

###################标签
class tag(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    addtime = db.Column(db.DateTime,nullable=False,index=True,default=datetime.datetime.now())
    tagName = db.Column(db.String(200), nullable=False)

    movies = db.relationship("movie",
                             secondary=movie_tag,
                             back_populates="tag_id")


###################电影
class movie(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200),nullable=False)
    info = db.Column(db.Text,nullable=False)
    logo = db.Column(db.String(200), nullable=False)
    star = db.Column(db.Float,nullable=False)
    playnum = db.Column(db.INTEGER,nullable=True)
    commentnum = db.Column(db.INTEGER, nullable=False)
    area = db.Column(db.String(200),nullable=False)
    release_time = db.Column(db.DateTime,nullable=False)
    length = db.Column(db.String(200),nullable=False)
    addtime = db.Column(db.DateTime,nullable=False,index=True,default=datetime.datetime.now())

    newtag  = db.Column(db.String(200),nullable=False)

    comments = db.relationship("comment", backref='movie', lazy="dynamic")
    collections = db.relationship("collection", backref='movie', lazy="dynamic")
    tag_id = db.relationship("tag",
                           secondary=movie_tag,
                           back_populates="movies"
                           )

#####################上映预告
class preview(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    logo = db.Column(db.String(100), nullable=False)
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.datetime.now())

    def __repr__(self):
        return "<preview(title='%s', logo='%s', addtime='%s')>" % (
            self.title, self.logo, self.addtime)


########################评论
class comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.datetime.now())


######################电影收藏
class collection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.datetime.now())
