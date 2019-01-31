#!/usr/bin/python3
""" Simple Flask web app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from os import environ
from operator import itemgetter
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(Exception):
    """close storage session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """/states response"""
    states_list = list(storage.all("State").values())
    return render_template('7-states_list.html', states_list=states_list)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """/states/<id> response"""
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        """db get state to cities relationship"""
        states_list = storage.all("State")
    else:
        """fs getter from cities"""
        states_list = storage.all(State)
    state_id = "State." + id
    if state_id in states_list:
        return render_template('9-states.html',
                               state=states_list.get(state_id))
    else:
        return render_template('9-states.html', state=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))
