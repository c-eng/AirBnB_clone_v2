#!/usr/bin/python3
""" Simple Flask web app"""
from flask import Flask
from flask import abort
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(Exception):
    """close storage session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """/states_list response"""
    states_list = sorted(storage.all("State").items())
    return render_template('7-states_list.html', states_list=states_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))
