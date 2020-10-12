"""Server for Bookbot recommendations app."""

from flask import Flask, render_template
import os
from secrets import KEY, SECRET

from goodreads import client
# create client instance to query Goodreads with python library
gc = client.GoodreadsClient(KEY, SECRET)

app = Flask(__name__)

# this is the homepage, for now it will have the form
@app.route('/')
def form_fillout():
    """Fill out the form to request a recommendation."""
    
    return render_template('form.html')


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
    app.run(host='0.0.0.0', debug=True)