from flask import Flask, redirect, request, render_template
import cgi
# import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html', title = 'index')


app.run()