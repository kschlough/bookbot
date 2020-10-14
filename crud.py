from model import db, User, RecommendationRequest, Genre

def create_user(name):
    """Create and return a new user."""

    user = User(name=name)

    db.session.add(user)
    db.session.commit()

    return user

# check this - do I pass genre in if it's drop-down and joined on the genre_id not name?
# when passing in genre: genre=Genre(genre_name='name'))
# have to pass in before genre: user=test_user
def create_recommendation(length, setting, genre):
    """Create and return a new recommendation."""

    recommendation = RecommendationRequest(length=length, setting=setting, genre=genre)

    db.session.add(recommendation)
    db.session.commit(recommendation)

    return recommendation

# again - is it right to create a genre? since they're pre-populated from drop-down not user added 
# but when user selects it's getting added tied to that rec, so yes?
def create_genre(genre_name):
    """Create and return a new genre."""

    genre_name = Genre(genre_name=genre_name)

    db.session.add(genre_name)
    db.session.commit(genre_name)

    return genre_name

if __name__ == '__main__':
    from server import app
    connect_to_db(app)