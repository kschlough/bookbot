"""Server for Bookbot recommendations app."""

from flask import Flask

app = Flask(__name__)

@app.route('/'):

@app.route('api/')


# crud: 
# create_user(name)
# create_recommendation(length, location, genre)
# create_genre(genre_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)