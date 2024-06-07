#!/usr/bin/python3
"""
This module initializes and runs a Flask web application to display
a list of states from a storage system. The states are listed in
alphabetical order on an HTML page.

Routes:
    /states_list: Displays an HTML page with the states listed
                  in alphabetical order.

Teardown:
    On teardown, the storage is closed to ensure no resource leaks.

Modules:
    - flask: Flask web framework
    - models: Custom module containing the storage system
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')