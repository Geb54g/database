from flask import Flask,render_template

app = Flask(__name__)


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



if __name__=='__main__':
    app.run(debug=True)
    