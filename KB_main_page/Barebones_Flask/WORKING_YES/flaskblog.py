from flask import Flask, render_template, url_for 
import os

IMG_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route("/")
@app.route("/home")
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test.png')
    
    return render_template("home.html", user_image = full_filename)
    # return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)