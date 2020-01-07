from flask import Flask,render_template,session,redirect,url_for
# 下面一行代码，定制了命令行
from flask_script import Manager
# 下面这些为了解决secret key (不知道什么玩意)
import os

#####
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect, CSRFError
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
	"""docstring for NameForm"""
	name = StringField('what is your name?',validators=[Required()])
	submit = SubmitField('Submit')
app = Flask(__name__)
manager = Manager(app)
# 与crsf 有关
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)
# 设置了方法，使用表单时常用
@app.route('/', methods = ['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		session['name']= form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))

@app.route('/hello/<username>')
def show_user_profile(username):
	return "hello %s" %username


def page_not_found(e):
	return render_template('404.html'),404
if __name__ == '__main__':
	manager.run()