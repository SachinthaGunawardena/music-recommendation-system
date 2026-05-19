import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

user_id = 1

history_query = f"""
SELECT
    songs.genre,
    songs.id,
    songs.track_name,
    songs.artist_name

FROM listening_history

JOIN songs
ON listening_history.song_id = songs.id

WHERE listening_history.user_id = {user_id}
"""

history_df = pd.read_sql(
    history_query,
    engine
)

print("\nUser Listening History:\n")
print(history_df.head())

favorite_genre = history_df['genre'].mode()[0]

print("\nFavorite Genre:\n")
print(favorite_genre)

recommendation_query = f"""
SELECT
    id,
    track_name,
    artist_name,
    genre

FROM songs

WHERE genre = '{favorite_genre}'

AND id NOT IN (

    SELECT song_id
    FROM listening_history
    WHERE user_id = {user_id}

)

LIMIT 10
"""

insert_recommendation_query = """
INSERT INTO recommendations (user_id, song_id)
VALUES (:user_id, :song_id)
"""


recommendations_df = pd.read_sql(
    recommendation_query,
    engine
)

print("\nRecommended Songs:\n")
print(recommendations_df)

with engine.connect() as connection:

    for _, row in recommendations_df.iterrows():

        connection.execute(
            text(insert_recommendation_query),
            {
                "user_id": user_id,
                "song_id": int(row['id'])
            }
        )

    connection.commit()

    print("\nRecommendations saved successfully!")
