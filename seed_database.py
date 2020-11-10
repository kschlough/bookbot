"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
from model import User, Genre, RecommendationRequest, RecommendationResponse
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
    bookbot_users = json.loads(f.read())

users_in_db = []
users = bookbot_users['items'][0]
for user in users:
    # use crud function to create user from each name in the json file
    db_user = crud.create_user(user)
    users_in_db.append(db_user)


# seed the genres table
with open('data/genres.json') as f:
    rec_genres = json.loads(f.read())

genres_in_db = []
genres = rec_genres['items']
for genre in genres:
    # use crud function to create genre for each genre in json file
    db_genre = crud.create_genre(genre)
    genres_in_db.append(db_genre)


# seed the recommendation requests table - 15 rec requests from 15 users
# instead of n in range 15: for each user in the users_in_db list
recommendation_reqs_in_db = []
for user in users_in_db:
    # pick a random genre for the user's request
    random_genre = choice(genres_in_db) 
    random_genre_id = random_genre.genre_id 

    # pick a random kw for the user's request from list 'KEYWORDS'
    random_kw = choice(KEYWORDS) 

    # assign to user.user_id - gives each user a recommendation
    rec_request = crud.create_recommendation(random_kw, random_genre_id, user.user_id)
    recommendation_reqs_in_db.append(rec_request)


# seed the recommendation responses table - 15 responses








# create recommendations, store in list
# create fake books
# books_in_db = []
# for book in book_recs_data:
#     title, author, setting, genre = (book['title'], book['author'], book['setting'], book['genre'])

#     db_book = crud.create_recommendation(setting, genre)
#     books_in_db.append(db_book)
