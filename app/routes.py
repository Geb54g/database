from fileinput import filename
import os
import secrets
from wsgiref import validate
from flask import render_template,url_for,flash,redirect
from app import app
from app.forms import RegistrationForm,LoginForm,UpdateAccountForm,PostForm
from app.models import User,Post
from flask_login import login_user

# from app.models import User,Post

posts = [
    {
        'author':'Gabriel Ndolo',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'May 2,2022'
    },
    {
        'author':'Gabriella Heinze',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'June 6,2022'
    }
]

@app.route("/")

@app.route("/home")

def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html',title ='About')


@app.route("/register",methods=['GET','POST'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title ='Register', form= form)



@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been login','success')
        return redirect(url_for('login'))
    return render_template('login.html',title ='Login', form= form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    
    
    return picture_fn


@app.route("/account",methods=['GET','POST'])
def account():
    form = UpdateAccountForm()
    return render_template('account.html',title ='Account',form=form)



@app.route("/post/new",methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created!','success')
        return redirect(url_for('home'))
    
    return render_template('posts.html',title ='New Posts',form=form)





