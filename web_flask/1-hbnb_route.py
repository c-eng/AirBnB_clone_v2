#!/usr/bin/python3
""" Simple Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """/ route response"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """/hbnb response"""
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))
