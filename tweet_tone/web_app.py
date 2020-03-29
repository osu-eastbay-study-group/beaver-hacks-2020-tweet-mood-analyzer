from flask import Flask, render_template


app = Flask(__name__)

# List of colors
tones = {
    "anger",
    "fear",
    "joy",
    "sadness",
    "analytical",
    "confident",
    "tentative",
    "none",
}

# Dummy Data
main_tweet = {
    'tweet_id': '1185017497482719233',
    'tone': 'joy',
    'intensity': '2',
    'children': [
        {
            'tweet_id': '1185303393801310208',
            'tone': 'joy',
            'intensity': '1',
        },
        {
            'tweet_id': '1185162876237029376',
            'tone': 'joy',
            'intensity': '1',
        },
        {
            'tweet_id': '1185282630285062144',
            'tone': 'joy',
            'intensity': '1',
        },
        {
            'tweet_id': '1185020345016827909',
            'tone': 'joy',
            'intensity': '1',
        }
    ]
}


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
