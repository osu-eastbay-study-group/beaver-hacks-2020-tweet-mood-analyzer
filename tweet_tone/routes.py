from flask import Flask, render_template
from tweet_tone import app
from tweet_tone.forms import TwitterLinkForm
from tweet_tone.models import Tweet, Child


@app.route("/<page_id>")
def search(page_id):
    """Page to enter in Tweet link."""
    return f"<h1>Page ID: {page_id}</h1>"


@app.route("/")
def home():
    """Home page."""
    return render_template('home.html',
                           main_tweet=main_tweet,
                           children=main_tweet['children'])
    # return search("home")  # TODO: Make home be a special case of search().


if __name__ == '__main__':
    app.run(debug=True)
