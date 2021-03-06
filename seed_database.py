"""Script to seed database."""

import os
import json
from random import choice, randint
import requests
import random

import crud
import model
from model import User, Genre, RecommendationRequest, RecommendationResponse
from model import db, connect_to_db
import server

os.system('dropdb book_recs')
os.system('createdb book_recs')

model.connect_to_db(server.app)
# model because we did import model, not from model import db 
# have to access db through model
model.db.create_all()

# random keywords to pull from for seeding requests
KEYWORDS = ["moscow",  
           "amos tversky", 
           "roman empire",
           "titanic",
           "foreign policy",
           "canada",
           "political science",
           "san francisco",
           "computer science",
           "artificial intelligence",
           "chicago",
           "ballet",
           "japan",
           "constitutional law",
           "linguistics"]


# seed the users table
with open('data/users.json') as f:
    bookbot_users = json.load(f)

users_in_db = []
users = bookbot_users['items'][0]
for user in users:
    # use crud function to create user from each name in the json file
    db_user = crud.create_user(user)
    users_in_db.append(db_user)

    db.session.add(db_user)
    db.session.commit()


# seed the genres table
with open('data/genres.json') as f:
    rec_genres = json.load(f)

genres_in_db = []
genres = rec_genres['items']
for genre in genres:
    # use crud function to create genre for each genre in json file
    db_genre = crud.create_genre(genre)
    genres_in_db.append(db_genre)

    db.session.add(db_genre)
    db.session.commit()


# seed the recommendation requests table - 15 rec requests from 15 users
# instead of n in range 15: for each user in the users_in_db list
recommendation_reqs_in_db = []
recommendation_responses_in_db = []
for user in users_in_db:
    # pick a random genre for the user's request
    random_genre = choice(genres_in_db) 
    random_genre_id = random_genre.genre_id 

    # pick a random kw for the user's request from list 'KEYWORDS'
    random_kw = choice(KEYWORDS) 

    # assign to user.user_id - gives each user a recommendation
    rec_request = crud.create_recommendation(random_kw, random_genre_id, user.user_id)
    recommendation_reqs_in_db.append(rec_request)

    db.session.add(rec_request)
    db.session.commit()

    # get the response in the same loop, all necessary info is available
    # search terms
    search_terms = {'q': f'{random_genre.genre_name}+{random_kw}'}

    response = requests.get('https://www.googleapis.com/books/v1/volumes', params=search_terms)
    results = response.json()
    num_results = int(len(results['items']))
    print(num_results)
    index = random.choice(range(0, num_results)) 
    book = results['items'][index]
    book_info = book['volumeInfo']
    book_title = book_info['title']

    # sets the author(s) if available
    if 'authors' not in book_info:
        book_author = "This book does not have listed authors. Bookbot suggests you consider Googling it."
    else:
        book_author = book_info['authors'][0]

    # get use id from username
    user = User.query.filter(User.name == user.name).first() 

    # get rec_id from rec requests
    rec_response = crud.create_recommendation_response(book_title, book_author, user.user_id, rec_request.rec_id)
    recommendation_responses_in_db.append(rec_response)

    db.session.add(rec_response)
    db.session.commit()
