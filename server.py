"""Server for Bookbot recommendations app."""

from flask import Flask, render_template, request
from model import connect_to_db
import os

import crud
from jinja2 import StrictUndefined

from secrets import KEY
from goodreads import client

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

# this is the homepage, for now it will have the form
@app.route('/')
def form_fillout():
    """Fill out the form to request a recommendation."""
    
    return render_template('form.html')

@app.route('/recommendation-request', methods=['POST'])
def new_recommendation():
    """Submit a new recommendation request from the user."""
    username = request.form['username']
    genre = request.form['genre']
    keyword = request.form['request-setting']
    length = request.form['request-length']

    return render_template('recommendation.html', 
                            username = username,
                            genre = genre,
                            keyword = keyword,
                            length = length)


# @app.route('https://www.goodreads.com/search/index.xml'
# print(search.books("Red Notice", 1, KEY, "title"))


# this is where the recommendation will be returned to, and where the form will submit to
# @app.route('/recommendation')
#     pass

# this is where the jsonify'd response from goodreads will be
# @app.route('api/')
#     pass


# crud: 
# create_user(name)
# create_recommendation(length, location, genre)
# create_genre(genre_name)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)