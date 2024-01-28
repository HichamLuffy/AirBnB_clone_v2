#!/usr/bin/python3
""" module numbr roote"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models import *

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ def doc """
    notfound = False
    if id is not None:
        state = storage.get(State, id)
        id = "States." + id
        with_id = True
        if state is None:
            notfound = True
    else:
        states = storage.all(State)
        with_id = False
    return render_template('9-states.html', states=states,
                           with_id=with_id, not_found=notfound)

@app.teardown_appcontext
def tear_db(e):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
