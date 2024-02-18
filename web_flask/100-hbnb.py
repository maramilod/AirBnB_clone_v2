#!/usr/bin/python3
"""
    100-hbnb module
    1 route renders a template with dynamic content
"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ colses the connectetion """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
        the hbnb_filters route that
        renders the first real full dynamic  page
    """
    states = storage.all(State).values()
    for state in states:
        if not hasattr(state, 'cities'):
            setattr(state, 'cities', state.cities)
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    for place in places:
        owner = users["User.{}".format(place.user_id)]
        setattr(place, "owner", "{} {}".format(owner.first_name,
                                               owner.last_name))
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
