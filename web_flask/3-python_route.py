#!/usr/bin/python3
""" script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    f_text = text.replace("_", " ")
    return "C {}".format(f_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyiscool(text):
    f_text = text.replace("_", " ")
    return "Python {}".format(f_text)


if __name__ == '__main__':
    app.run()
