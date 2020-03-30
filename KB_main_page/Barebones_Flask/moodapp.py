from flask import Flask, escape, request, render_template, url_for
app = Flask(__name__)


title = "potato"

@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html', title=title)

@app.route('/about')
def about():
    return render_template('about.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)