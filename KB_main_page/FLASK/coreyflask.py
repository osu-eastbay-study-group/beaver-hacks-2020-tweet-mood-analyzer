from flask import Flask, escape, request, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Kyle bell',
        'title': 'blog post',
        'content': 'post stuff',
        'date_posted': 'today',
    }
]

title = "potato"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)