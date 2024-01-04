#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


def func(obj):
    """
    To sort.
    """
    return obj.name


@app.route('/states_list', strict_slashes=False)
def get_states():
    """
    The states route.
    """
    states = sorted(storage.all(State).values(), key=func)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Teardown function.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
