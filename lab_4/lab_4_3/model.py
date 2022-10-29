import pandas as pd


def get_publisher(conn):
    return pd.read_sql("SELECT * FROM publisher", conn)


def get_author(conn):
    return pd.read_sql("SELECT * FROM author", conn)


def get_genre(conn):
    return pd.read_sql("SELECT * FROM genre", conn)


def card(conn, publishers: list, genres: list, authors: list):
    authors = tuple(authors)
    genres = tuple(genres)
    publishers = tuple(publishers)
    return pd.read_sql('''
        SELECT
            book_id,
        	title AS 'Название',
        	group_concat(DISTINCT author_name) AS 'Авторы',
        	genre_name AS 'Жанр',
        	publisher_name AS 'Издательство',
            year_publication AS 'Год_издания',
            available_numbers AS 'Количество'
        FROM book
        JOIN genre USING(genre_id)
        JOIN publisher USING(publisher_id)
        JOIN book_author USING(book_id)
        JOIN author USING(author_id)
        GROUP BY book_id
        HAVING (genre_id IN %(genres)s)OR NOT IN %(genres)s)
            AND (publisher_id IN %(publishers)s OR NOT IN %(publishers)s)
            AND (author_id IN %(authors)s OR NOT IN %(authors)s)
        ORDER BY
            title,
            available_numbers DESC,
            genre_name,
            year_publication DESC 
    ''', conn, params={"authors": authors, "genres": genres, "publishers": publishers})
