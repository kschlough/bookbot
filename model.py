"""Models for Bookbot recommendations app."""
# createdb book_recs

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        """Show info about the user."""

        return f'<User user_id={self.user_id} name={self.name}>'


class Genre(db.Model):
    """A genre."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Show info about the genre."""

        return f'<Genre genre_id={self.genre_id} genre_name={self.genre_name}'


class RecommendationRequest(db.Model):
    """A recommendation request."""

    __tablename__ = "recommendation_requests"

    rec_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    setting = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))

    user = db.relationship('User', backref='recommendation_requests')
    genre = db.relationship('Genre', backref='recommendation_requests')

    def __repr__(self):
        """Show info about the recommendation request."""

        return f'<Recommendation rec_id={self.rec_id} user_id={self.user_id} genre_id={self.genre_id} setting={self.setting}>'


class RecommendationResponse(db.Model):
    """A recommendation response."""

    __tablename__ = "recommendation_responses"

    resp_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rec_id = db.Column(db.Integer, db.ForeignKey('recommendation_requests.rec_id'))
    book_title = db.Column(db.String)
    book_author = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref='recommendation_responses')
    rec = db.relationship('RecommendationRequest', backref='recommendation_responses')

    def __repr__(self):
        """Show info about the recommendation response."""

        return f'Recommendation response resp_id={self.resp_id} rec_id={self.rec_id} book_title={self.book_title} user_id={self.user_id}'


def connect_to_db(flask_app, db_uri='postgresql:///book_recs', echo=True):
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