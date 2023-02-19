from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello')
def hello():
    return "Hello, World"


@app.route('/about')
def about():
    return "About page\n" \
           "author Petro S.\n" \
           "vers 1.0"

app.run()