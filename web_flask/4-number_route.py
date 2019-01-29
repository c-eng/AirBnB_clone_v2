#!/usr/bin/python3
""" Simple Flask web app"""
from flask import Flask
from flask import abort
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """/ route response"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """/hbnb response"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    """/c/ response"""
    return 'C {}'.format(text).replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """/python/ response"""
    return 'Python {}'.format(text).replace('_', ' ')

@app.route('/number/<n>', strict_slashes=False)
def number(n=""):
    """/number response"""
    if n.isdigit():
        return '{} is a number'.format(n)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))
