from app import app
from flask import render_template, request
from utils import get_db_connection
from models.search_model import get_genre, get_author, get_publisher, card


@app.route('/search', methods=['get', 'post'])
def search():
    conn = get_db_connection()
    df_author = get_author(conn)
    df_publisher = get_publisher(conn)
    df_genre = get_genre(conn)

    # if request.form.get('clear'):
    #     genres = ()
    #     publishers = ()
    #     authors = ()
    # else:
    #     genres = tuple(request.form.getlist('genre_id'))
    #     publishers = tuple(request.form.getlist('publisher_id'))
    #     authors = tuple(request.form.getlist('author_id'))

    genres = (3,2,1)
    authors = (2, 3, 4, 5)
    publishers = ()

    df_card = card(conn, publishers, genres, authors)

    html = render_template(
        'search.html',
        authors=df_author,
        publishers=df_publisher,
        genres=df_genre,
        card=df_card,
        sel_authors=authors,
        sel_publishers=publishers,
        sel_genres=genres,
        len=len
    )
    return html
