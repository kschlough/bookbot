"""Models for book recommendations app Bookbot."""

from flask_sqlalchemy import SQLALchemy 

db = SQLALchemy()

class User(db.Model):
    """A user."""

    __tablename__ = users

    user_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)



class RecommendationRequest(db.Model):
    """A recommendation request."""

    __tablename__ = recommendation_requests

    rec_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)



class Genre(db.Model):
    """A genre."""

    __tablename__ = genres

    genre_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

