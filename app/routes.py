from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')
    
@app.route('/register')
def register():
    """Register URL"""
    return render_template('register.html', title='Register Page')

@app.route('/login')
def login():
    """Login URL"""
    return render_template('login.html', title='Login Page')
    