from flask import Flask, render_template, url_for
from tweet_tone import app
from tweet_tone.forms import TwitterLinkForm
from tweet_tone.models import Tweet, Child
import os

IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route("/childtweet")
def search():
    """Page to enter in Tweet link."""
    return render_template("childtweet.html")

@app.route("/")
@app.route("/home")
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test.png')
    return render_template("home.html", user_image = full_filename)
    # return render_template('home.html')
