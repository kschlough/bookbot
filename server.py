"""Server for Bookbot recommendations app."""

from flask import Flask, render_template, request, jsonify, redirect
from model import connect_to_db
import requests # python library - outgoing request
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
    keyword = request.form['request-kw']
    length = request.form['request-length']

    search_terms = {'q': f'{genre}+{keyword}'}

    response = requests.get('https://www.googleapis.com/books/v1/volumes', params=search_terms)
    results = response.json()
    book = results['items'][0]
    book_info = book['volumeInfo']
    book_title = book_info['title']
    # book_author = book_info['authors']
    # book_genre = book_info['categories']
    # page_count = book_info['pageCount']
    # average_rating = book_info['averageRating']
    description = book_info['description'] 
    image_url = book_info['imageLinks']['thumbnail']

    return render_template('recommendation.html', 
                            username = username,
                            genre = genre,
                            keyword = keyword,
                            length = length,
                            book_title = book_title,
                            # book_author = book_author,
                            # book_genre = book_genre,
                            # page_count = page_count,
                            # average_rating = average_rating,
                            description = description,
                            image_url = image_url)

@app.route('/api/recommendation')
# @app.route('https://www.googleapis.com/books/v1/volumes?q=`${search_terms}`', methods=['GET'])
# def google_books_return():
#     return jsonify(response)

# 
# print(search.books("Red Notice", 1, KEY, "title"))


# this is where the recommendation will be returned to, and where the form will submit to
# @app.route('/recommendation')
#     pass

# this is where the jsonify'd response from goodreads will be
@app.route('/api/recommendation.json', methods = ['GET'])
def recommendation_jsonify():
    """Return a recommendation-info dictionary for the user's current request."""

    username = request.args.get('username')
    return jsonify(username)

# crud: 
# create_user(name)
# create_recommendation(length, location, genre)
# create_genre(genre_name)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)