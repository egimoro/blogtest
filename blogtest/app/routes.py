from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():    
    user={'username':'Lopingemma'}
    return render_template('index.html',title='Home',user=user)
