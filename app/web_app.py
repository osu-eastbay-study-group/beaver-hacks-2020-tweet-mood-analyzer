from flask import Flask


app = Flask(__name__)


@app.route("/<page_id>")
def search(page_id):
    """Page to enter in Tweet link."""
    return "<h1>Search</h1>"


@app.route("/")
def home():
    """Home page."""
    return "<h1>Home</h1>"
    # return search("home")  # TODO: Make home be a special case of search().


if __name__ == '__main__':
    app.run(debug=True)
