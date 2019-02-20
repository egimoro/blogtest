from app import app
from flask import render_template

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
