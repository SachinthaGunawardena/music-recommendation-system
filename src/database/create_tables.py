from sqlalchemy import create_engine, text

import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

drop_tables_query = """

DROP TABLE IF EXISTS recommendations;
DROP TABLE IF EXISTS listening_history;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS songs;

"""

songs_table = """

CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    track_name TEXT,
    artist_name TEXT,
    genre TEXT,
    release_date TEXT
);

"""

users_table = """

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE
);

"""

history_table = """

CREATE TABLE listening_history (

    history_id SERIAL PRIMARY KEY,

    user_id INTEGER REFERENCES users(user_id),

    song_id INTEGER REFERENCES songs(id),

    listened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""

recommendations_table = """

CREATE TABLE recommendations (

    recommendation_id SERIAL PRIMARY KEY,

    user_id INTEGER REFERENCES users(user_id),

    song_id INTEGER REFERENCES songs(id),

    recommended_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""

with engine.connect() as connection:

    connection.execute(text(drop_tables_query))

    connection.execute(text(songs_table))
    connection.execute(text(users_table))
    connection.execute(text(history_table))
    connection.execute(text(recommendations_table))

    connection.commit()

print("Professional relational tables created successfully!")