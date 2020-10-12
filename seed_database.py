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
model.db.create_all()

# load book recommendation data from JSON file
with open('data/book_recs.json') as f:
    book_recs_data = json.loads(f.read())


# create recommendations, store in list
# create fake recommendations


# create 10 users, each user makes 10 recommendations


