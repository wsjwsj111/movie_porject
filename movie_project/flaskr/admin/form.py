from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo,Regexp,ValidationError
from flaskr.admin import model


class RegisterForm(FlaskForm):
    username = StringField(label="用户名",validators=[DataRequired("用户名不能为空！"),Regexp("^[a-zA-Z_]\w{3,19}$",flags=0,message="用户名格式错误，请重新输入！")],render_kw={"placeinfo":"用户名由4-20位字母/数字/下划线组成,数字不能开头"})
    pwd = PasswordField(label="密码",validators=[DataRequired("密码不能为空！"),Regexp("^\S{6,16}$",flags=0,message="密码格式错误，请重新输入！")],render_kw={"placeinfo":"密码为6-16位有效字符（非空白字符）"})
    name = StringField(label="昵称",validators=[DataRequired("昵称不能为空！"),Regexp("^[a-zA-Z_]\w{3,19}$",flags=0,message="昵称格式错误，请重新输入！")],render_kw={"placeinfo":"昵称由4-20位字母/数字/下划线组成,数字不能开头"})
    email = StringField(label="邮箱",validators=[DataRequired("邮箱不能为空！"),Email('邮箱格式不正确！')],render_kw={"placeinfo":"邮箱的标准样式"})
    phone = StringField(label="手机号",validators=[DataRequired("手机号不能为空！"),Regexp("^1[3578]\d{9}$",flags=0,message="手机号格式错误，请重新输入！")],render_kw={"placeinfo":"手机号由11位数字组成"})
    pwdagain = PasswordField(label="确认密码",validators=[DataRequired("确认密码不能为空！"),EqualTo("pwd",message="两次密码输入不一致，请重新输入！")],render_kw={"placeinfo":"输入与上面一样的密码！"})
    submit = SubmitField("注册")

    def validate_username(self,field):
        if model.user.query.filter_by(username=field.data).first():
            raise ValidationError("用户名已存在")

    def validate_email(self, field):
        if model.user.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱已存在")

    def validate_phone(self, field):
        if model.user.query.filter_by(phone=field.data).first():
            raise ValidationError("手机号已存在")

