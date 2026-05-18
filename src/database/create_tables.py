from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

songs_table = """
CREATE TABLE IF NOT EXISTS songs (
    id SERIAL PRIMARY KEY,
    track_name TEXT,
    artist_name TEXT,
    genre TEXT,
    release_date TEXT
);
"""

users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE
);
"""

history_table = """
CREATE TABLE IF NOT EXISTS listening_history (
    history_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    song_id INTEGER,
    listened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

recommendations_table = """
CREATE TABLE IF NOT EXISTS recommendations (
    recommendation_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    song_id INTEGER,
    recommended_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

with engine.connect() as connection:

    connection.execute(text(songs_table))
    connection.execute(text(users_table))
    connection.execute(text(history_table))
    connection.execute(text(recommendations_table))

    connection.commit()

print("All tables created successfully!")