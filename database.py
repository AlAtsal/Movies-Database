import datetime
import sqlite3

CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    title TEXT, 
    release_timestamp REAL, 
    watched INTEGER
);"""

INSERT_MOVIES = """INSERT INTO movies (
    title, 
    release_timestamp, 
    watched) 
    VALUES(?, ?, 0) ;"""
    
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING = " SELECT * FROM movies WHERE release_timestamp > ? ;"
SELECT_WATCHED = " SELECT * FROM movies WHERE watched = 1 ;"
WATCH_MOVIE = "UPDATE movies SET watched = 1 WHERE title = ? ;"

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movies(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES,(title, release_timestamp))


def get_movies(heading):
    with connection:
        cursor = connection.cursor()
        if heading == "Upcoming":
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING, (today_timestamp, ))
        elif heading == "All":
            cursor.execute(SELECT_ALL_MOVIES)
        else:
            cursor.execute(SELECT_WATCHED)
        return cursor.fetchall()
     


def watch_movie(title):
    with connection:
        cursor = connection.cursor()
        cursor.execute(WATCH_MOVIE, (title,))