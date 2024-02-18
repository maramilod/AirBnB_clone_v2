#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnh():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    f_text = text.replace("_", " ")
    return "C {}".format(f_text)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyiscool(text):
    f_text = text.replace("_", " ")
    return "Python {}".format(f_text)


@app.route("/number/<int:n>", strict_slashes=False)
def onlynum(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
