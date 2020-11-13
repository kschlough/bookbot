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

    ############ add handling here later for category to match form/genre input




####################################
# changed to above doing in one loop - commenting out below for now
# seed the recommendation responses table - 15 responses
# for rec in recommendation_reqs_in_db:
#     genre_id = rec.genre_id
#     kw = rec.setting

#     # crud.create_recommendation_response(#title, author, user_id)
#     crud.create_recommendation_response(rec.user_id)








# create recommendations, store in list
# create fake books
# books_in_db = []
# for book in book_recs_data:
#     title, author, setting, genre = (book['title'], book['author'], book['setting'], book['genre'])

#     db_book = crud.create_recommendation(setting, genre)
#     books_in_db.append(db_book)
