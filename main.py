from flask import Flask, redirect, request, render_template
import cgi
# import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/submit", methods = ['POST'])
def submit():
    name = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    error = ''
    if(name == '' or password == '' or verify_password == '' or email == ''):
        error = "This is a fail"
        return redirect("/?error=" + error)
    return render_template('welcome.html', username = name, error = error)
@app.route("/")
def index():
    encoded_error = request.args.get("error")

    return render_template('home.html', title = 'Index', error = encoded_error)




app.run()