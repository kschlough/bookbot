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
                            book_title = book_title,
                            # book_author = book_author,
                            # book_genre = book_genre,
                            # page_count = page_count,
                            # average_rating = average_rating,
                            description = description,
                            image_url = image_url)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)