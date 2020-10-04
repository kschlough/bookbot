"""Models for book recommendations app Bookbot."""
# createdb book_recs

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String)

    # recommendation_request = db.relationship('RecommendationRequest')

    def __repr__(self):
        """Show info about the user."""

        return f'<User user_id={self.user_id} name={self.name}>'


# class RecommendationRequest(db.Model):
#     """A recommendation request."""

#     __tablename__ = "recommendation_requests"

#     rec_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)
#     length = db.Column(db.Integer, nullable=False)
#     location = db.Column(db.Text)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))

#     user = db.relationship('User')
#     genre = db.relationship('Genre')

#     def __repr__(self):
#         return f'<Recommendation rec_id={self.rec_id} user_id={self.user_id} genre_id={genre_id} length={length} location={location}>'


# class Genre(db.Model):
#     """A genre."""

#     __tablename__ = "genres"

#     genre_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)

#     genre = db.Column(db.String, )
#     rec_id = db.Column(db.Integer, db.ForeignKey('recommendation_requests.rec_id'))

#     recommendation_request = db.relationship('RecommendationRequest')

#     def __repr__(self):
#         return f'<Genre genre_id={self.genre_id} genre={self.genre} rec_id={self.rec_id}>'


# copied from ratings lab

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)