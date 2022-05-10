from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm

app = Flask(__name__)

app.config['SECTRET_KEY'] = '76bfd1aa0261f9781a899f00d901908c'

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


@app.route("/register")

def register():
    form = RegistrationForm()
    return render_template('register.html',title ='Register', form= form)




if __name__=='__main__':
    app.run(debug=True)
    