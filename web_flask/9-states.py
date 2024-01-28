#!/usr/bin/python3
""" module numbr roote"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models import *

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """ def states """
    states = storage.all(State)
    state_id = "State." + id if id else None
    return render_template("9-states.html", states=states, state_id=id)


@app.teardown_appcontext
def tear_db(e):
    """ tear db """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
