#!/usr/bin/python3
""" Simple Flask web app"""
from flask import Flask
from flask import abort
from flask import render_template
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

@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n=""):
    """/number_template response"""
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """/number_odd_or_even response"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))
