from flask import render_template,url_for,flash,redirect
from app import app
from app.forms import RegistrationForm,LoginForm,UpdateAccountForm
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

@app.route("/account")
def account():
    form = UpdateAccountForm()
    return render_template('account.html',title ='Account',form=form)





