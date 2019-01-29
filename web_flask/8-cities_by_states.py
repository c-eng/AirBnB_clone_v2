#!/usr/bin/python3
""" Simple Flask web app"""
from flask import Flask
from flask import abort
from flask import render_template
from models import storage
from os import environ
from operator import itemgetter
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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """/cities_by_state response"""
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        """db get state to cities relationship"""
        states_list = sorted(storage.all("State").items())
    else:
        """fs getter from cities"""
        states_list = sorted(storage.all(State).items())
    cities_list = []
    for state_id, state in states_list:
        for city in state.cities:
            cities_list.append([state.id, city.name])
    cities_list = sorted(cities_list, key=itemgetter(1))
    return render_template('8-cities_by_states.html', states_list=states_list,
                           cities_list=cities_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))
