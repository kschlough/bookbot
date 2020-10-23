from model import db, User, RecommendationRequest, Genre

def create_user(name):
    """Create and return a new user."""

    user = User(name=name)

    db.session.add(user)
    db.session.commit()

    return user


def create_recommendation(setting, genre):
    """Create and return a new recommendation."""

    recommendation = RecommendationRequest(setting=setting, genre=genre)

    db.session.add(recommendation)
    db.session.commit(recommendation)

    return recommendation


def create_genre(genre_name):
    """Create and return a new genre."""

    genre_name = Genre(genre_name=genre_name)

    db.session.add(genre_name)
    db.session.commit(genre_name)

    return genre_name

if __name__ == '__main__':
    from server import app
    connect_to_db(app)