"""Server for Bookbot recommendations app."""

from flask import Flask
import os

app = Flask(__name__)
SECRET_KEY = os.environ["SECRET_KEY"]

# this is the homepage, for now it will have the form
@app.route('/'):
def form_fillout():
    """Fill out the form to request a recommendation."""

# this is where the recommendation will be returned to, and where the form will submit to
@app.route('/recommendation'):

# this is where the jsonify'd response from goodreads will be
@app.route('api/')


# crud: 
# create_user(name)
# create_recommendation(length, location, genre)
# create_genre(genre_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)