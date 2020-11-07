"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb book_recs')
os.system('createdb book_recs')

model.connect_to_db(server.app)
# model because we did import model, not from model import db 
# have to access db through model
model.db.create_all()

# load book recommendation data from JSON file
# with open('data/book_recs.json') as f:
#     book_recs_data = json.loads(f.read())

    # this is just what you seed the database with
    # hardcode if needed - can be easier to demo with hardcoded data
    # api connection - probably has json data, see what they give back & write python that takes it & puts in db
    # can also have a SQL file that inserts data
    # python library faker gives fake data, another option
    # pgm postgres tool to input data (or insert statements in SQL file)

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
for user in users_in_db:
    # pick a random genre for the user's request
    random_genre = choice(genres_in_db) # ex: "Art"
    request_genre = Genre.query.filter(Genre.genre_name == random_genre).first() # ex: "<Genre genre_id=3 genre_name=Art"
    random_genre_id = request_genre.genre_id # ex: 3

    # pick a random kw for the user's request from list 'KEYWORDS'
    random_kw = choice(KEYWORDS) # ex: "moscow"

    # pick a random user to assign the request to
    

    crud.create_recommendation(setting=random_kw, genre_id=random_genre_id, user_id=)


# seed the recommendation responses table - 15 responses






# create recommendations, store in list
# create fake books
# books_in_db = []
# for book in book_recs_data:
#     title, author, setting, genre = (book['title'], book['author'], book['setting'], book['genre'])

#     db_book = crud.create_recommendation(setting, genre)
#     books_in_db.append(db_book)
