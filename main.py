from flask import Flask, redirect, request, render_template
import cgi
# import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['POST'])
def submit():
    #defining variables
    name = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    error = False
    error_username = ''
    error_password = ''
    error_verify_password = ''
    error_email = ''
    
    if(name == ''):
        error = True
        error_username = "Please enter a valid username"
    if(password == ''):
        error = True
        error_password = "Please enter a valid password"
    if(verify_password == ''):
        error = True
        error_verify_password = "Please enter a valid password"
    if(len(name) < 3 or len(name) > 20):
        error = True
        error_username = "Please ensure username is 3 or more characters but no more than 20"
    if(len(password) < 3 or len(password) > 20):
        error = True
        error_password = "Please ensure password is 3 or more characters but no more than 20"
    if(password != verify_password):
        error = True
        error_verify_password = "Passwords must match"
        error_password = "Passwords must match"
    if(' ' in name):
        error = True
        error_username = "Username cannot contain a space"
    if(' ' in password):
        error = True
        error_password = "Password cannot contain a space"
    if(email != ''):
        if(len(email) < 3 or len(email) > 20):
            error = True
            error_email = "Please ensure email is 3 or more characters but no more than 20"
        if(' ' in email):
            error = True
            error_email = "Email cannot contain a space"
        if('@' in email and email.count('@') > 1):
            error = True
            error_email = "Please enter a valid email address"
        if('@' not in email):
            error = True
            error_email = "Please enter a valid email address"
        if('.' in email and email.count('.') > 1):
            error = True
            error_email = "Please enter a valid email address"
        if('.' not in email):
            error = True
            error_email = "Please enter a valid email address"


        
    
    if(error == True):
        return render_template('home.html', title = 'Index', error_username = error_username,
        error_password = error_password, error_verify_password = error_verify_password,
        error_email = error_email, username = name, email = email)
    else:
        return render_template('welcome.html', title = 'Welcome', username = name)
@app.route("/")
def index():
    return render_template('home.html', title = 'Index')




app.run()