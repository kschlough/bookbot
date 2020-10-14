"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

from goodreads import client
# create client instance to query Goodreads with python library
gc = client.GoodreadsClient(KEY, SECRET)

os.system('dropdb book_recs')
os.system('createdb book_recs')

model.connect_to_db(server.app)
model.db.create_all()

# load book recommendation data from JSON file
with open('data/book_recs.json') as f:
    book_recs_data = json.loads(f.read())

    # this is just what you seed the database with
    # hardcode if needed - can be easier to demo with hardcoded data
    # api connection - probably has json data, see what they give back & write python that takes it & puts in db
    # can also have a SQL file that inserts data
    # python library faker gives fake data, another option
    # pgm postgres tool to input data (or insert statements in SQL file)


# create recommendations, store in list
# create fake books
books_in_db = []
for book in book_recs_data:
    title, author, setting, genre = (book['title'], book['author'], book['setting'], book['genre'])
    if length > 500:
        length = 'long'
    elif length < 500 and length > 200:
        length = 'medium'
    elif length < 200:
        lengh = 'short'

    db_book = crud.create_recommendation(length, setting, genre)
    books_in_db.append(db_book)


# create 10 users, each user makes 10 recommendations


print(search.books("Red Notice", 1, KEY, "title"))