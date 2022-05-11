from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
from forms import validators

app = Flask(__name__)

app.config['SECRET_KEY'] = '76bfd1aa0261f9781a899f00d901908c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


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
        return redirect(url_for('home'))
    return render_template('login.html',title ='Login', form= form)





if __name__=='__main__':
    app.run(debug=True)
    