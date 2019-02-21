from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():    
    user={'username':'Lopingemma'}
    posts=[
        {
            'author':{'username':'Klohn'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Dosan'},
            'body':'The Avengers are stale!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='Sign In',form=form)
    