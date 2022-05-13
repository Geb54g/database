from fileinput import filename
import os
import secrets
from wsgiref import validate
from flask import render_template,url_for,flash,redirect
from app import app,db,bcrypt
from app.forms import RegistrationForm,LoginForm,UpdateAccountForm,PitchForm
from app.models import User,Pitch
from flask_login import login_user

# from app.models import User,Post

pitches = [
    {
        'author':'Shawn Brook',
        'title':' Product Pitch',
        'content':'pitch content',
        'date_posted':'May 2,2022'
    },
    {
        'author':'Jane Heinze',
        'title':'Promotional pitch ',
        'content':'pitch content',
        'date_posted':'October 6,2022'
    },
     {
        'author':'Wayne Hon',
        'title':'Pick-up pitch ',
        'content':' Are you a parking ticket? Cause you have got fine written all over you',
        'date_posted':'Match 11,2022'
    },
      {
        'author':'Luke Woods',
        'title':'Business pitch ',
        'content':'pitch content',
        'date_posted':'April 4,2022'
    }
]

@app.route("/")

@app.route("/home")

def home():
    return render_template('home.html', pitches = pitches)


@app.route("/about")
def about():
    return render_template('about.html',title ='About')


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Your account has been created!','success')
        return redirect(url_for('login'))
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



@app.route("/pitch/new",methods=['GET','POST'])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        flash('Your pitch has been created!','success')
        return redirect(url_for('home'))
    
    return render_template('pitches.html',title ='New Pitches',form=form)





