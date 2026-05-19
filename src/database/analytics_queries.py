import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

popular_songs_query = """
SELECT
    song_id,
    COUNT(*) AS play_count
FROM listening_history
GROUP BY song_id
ORDER BY play_count DESC
LIMIT 10;
"""

popular_songs_df = pd.read_sql(
    popular_songs_query,
    engine
)

print("\nTop 10 Most Played Songs:\n")
print(popular_songs_df)

active_users_query = """
SELECT
    user_id,
    COUNT(*) AS total_listens
FROM listening_history
GROUP BY user_id
ORDER BY total_listens DESC;
"""
active_users_df = pd.read_sql(
    active_users_query,
    engine
)

print("\nMost Active Users:\n")
print(active_users_df)

favorite_genres_query = """
SELECT
    songs.genre,
    COUNT(*) AS total_plays
FROM listening_history

JOIN songs
ON listening_history.song_id = songs.id

GROUP BY songs.genre
ORDER BY total_plays DESC
LIMIT 10;
"""

favorite_genres_df = pd.read_sql(
    favorite_genres_query,
    engine
)

print("\nTop Genres:\n")
print(favorite_genres_df)
