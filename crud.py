from model import db, User, Genre, RecommendationRequest, RecommendationResponse

def create_user(name):
    """Create and return a new user."""

    user = User(name=name)

    db.session.add(user)
    db.session.commit()

    return user


def create_genre(genre_name):
    """Create and return a new genre."""

    genre_name = Genre(genre_name=genre_name)

    db.session.add(genre_name)
    db.session.commit(genre_name)

    return genre_name


def create_recommendation(setting, genre_id, user_id):
    """Create and return a new recommendation."""

    recommendation = RecommendationRequest(setting=setting, 
                                            genre_id=genre_id,
                                            user_id=user_id)

    db.session.add(recommendation)
    db.session.commit(recommendation)

    return recommendation


def create_recommendation_response(book_title, book_author, user_id):
    """Create and return a new recommendation response."""

    recommendation_response = RecommendationResponse(book_title=book_title,
                                                    book_author=book_author,
                                                    user_id=user_id)

    return recommendation_response


if __name__ == '__main__':
    from server import app
    connect_to_db(app)