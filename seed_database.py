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

# seed the users table
with open('data/users.json') as f:
    bookbot_users = json.loads(f.read())

users_in_db = []
users = bookbot_users['items'][0]
for user in users:
    # use crud function to create user from each name in the json file
    crud.create_user(user)


# seed the genres table
with open('data/genres.json') as f:
    rec_genres = json.loads(f.read())

genres_in_db = []
genres = rec_genres['items']
for genre in genres:
    # use crud function to create genre for each genre in json file
    crud.create_genre(genre)

# create recommendations, store in list
# create fake books
# books_in_db = []
# for book in book_recs_data:
#     title, author, setting, genre = (book['title'], book['author'], book['setting'], book['genre'])

#     db_book = crud.create_recommendation(setting, genre)
#     books_in_db.append(db_book)


# create 10 users, each user makes 10 recommendations

#########################
# logic:
# when user hits submit on the form:
    # save the user info & request info to the db using crud
    # save a snapshot of the db at the given time?
# on load of the json data displaying in the new page:
    # save the json info displayed into the db
    # save a snap of the db?
