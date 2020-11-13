"""Server for Bookbot recommendations app."""

from flask import Flask, render_template, request, jsonify, redirect
from model import connect_to_db, db
from model import User, Genre, RecommendationRequest, RecommendationResponse
import requests # python library - outgoing request
import random # for random choice of book from API response
import os
import json

import crud
from jinja2 import StrictUndefined

from secrets import KEY

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined


# this is the homepage, for now it will have the form
@app.route('/')
def form_fillout():
    """Fill out the form to request a recommendation."""
    
    # parse through the genres.json and put into a list
    with open('data/genres.json') as f:
        rec_genres = json.load(f)

    genres_list = []
    genres = rec_genres['items']
    for genre in genres:
        genres_list.append(genre)


    return render_template('form.html',
                            genres_list = genres_list)


@app.route('/recommendation-request', methods=['POST'])
def new_recommendation():
    """Submit a new recommendation request from the user."""
    username = request.form['username']
    genre = request.form['genre']
    keyword = request.form['request-kw']

    search_terms = {'q': f'{genre}+{keyword}'}
    # changed from {genre}{keyword} to adding + as API requested


    # add crud function for user's request:
    # add user:
    db_user = crud.create_user(username)
    # get user id:
    user_name = User.query.filter(User.name == db_user.name).first() 
    user_id = user_name.user_id
    # find genre id:
    request_genre = Genre.query.filter(Genre.genre_name == genre).first() 
    genre_id = request_genre.genre_id
    # submit rec request:
    rec_request = crud.create_recommendation(keyword, genre_id, user_id)
    # commit to db
    db.session.add(rec_request)
    db.session.commit()


    response = requests.get('https://www.googleapis.com/books/v1/volumes', params=search_terms)
    results = response.json()
    num_results = int(len(results['items']))

    # while loop until genre matches user's selected genre
    index = random.choice(range(0, num_results)) 
    while results['items'][index]['volumeInfo']['categories'][0] != genre:
        # get another random book
        index = random.choice(range(0, num_results)) 

    # out of the loop with a match:
    book = results['items'][index]
    book_info = book['volumeInfo']
    book_title = book_info['title']

    # sets maturity
    if book_info['maturityRating'] == "MATURE":
        maturity_rating = "Caution! This book may contain mature themes."
    else:
        maturity_rating = "This book is not rated mature."      

    # sets the description if available
    if 'description' not in book_info:
        description = "This book does not have a description. Bookbot suggests you consider Googling it."
    else:
        description = book_info['description']

    # sets the author(s) if available
    if 'authors' not in book_info:
        book_author = "This book does not have listed authors. Bookbot suggests you consider Googling it."
    else:
        book_author = book_info['authors'][0]
        # add handling here for multiple - right now just [0]

    # sets the categories if available (it should be bc has to match line 58, but this is extra caution)
    # added handling line 58 for category to match form/genre input
    if 'categories' not in book_info:
        book_genre = "Oops! This book doesn't appear to have specified genre(s). Bookbot suggests you consider Googling it to make sure this recommendation fits your desired genre."
    else:
        book_genre = book_info['categories'][0] 

    # sets the page count if available
    if 'pageCount' not in book_info:
        page_count = "This book does not have a specified page count. Bookbot suggests you consider listening to the audiobook if you are unsure your attention span will be up to par."
    else:
        page_count = book_info['pageCount']

    # sets the average rating if available
    if 'averageRating' not in book_info:
        average_rating = "This book does not have an average rating."
    else:
        average_rating = book_info['averageRating']    

    image_url = book_info['imageLinks']['thumbnail']

    return render_template('recommendation.html', 
                            username = username,
                            genre = genre,
                            keyword = keyword,
                            book_title = book_title,
                            maturity_rating = maturity_rating,
                            book_author = book_author,
                            book_genre = book_genre,
                            page_count = page_count,
                            average_rating = average_rating,
                            description = description,
                            image_url = image_url)


@app.route('/recent-requests')
def show_recents():
    return render_template('recents.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)