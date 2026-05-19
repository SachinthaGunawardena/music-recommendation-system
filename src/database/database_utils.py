import pandas as pd

from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

def get_user_history(user_id):

    query = f"""
    SELECT
        songs.id,
        songs.track_name,
        songs.artist_name,
        songs.genre

    FROM listening_history

    JOIN songs
    ON listening_history.song_id = songs.id

    WHERE listening_history.user_id = {user_id}
    """

    df = pd.read_sql(query, engine)

    return df

def get_favorite_genre(user_id):

    history_df = get_user_history(user_id)

    favorite_genre = history_df['genre'].mode()[0]

    return favorite_genre

def get_recommendations(user_id, limit=10):

    favorite_genre = get_favorite_genre(user_id)

    query = f"""
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

    LIMIT {limit}
    """

    recommendations_df = pd.read_sql(query, engine)

    return recommendations_df

def save_recommendations(user_id, recommendations_df):

    insert_query = """
    INSERT INTO recommendations (user_id, song_id)
    VALUES (:user_id, :song_id)
    """

    with engine.connect() as connection:

        for _, row in recommendations_df.iterrows():

            connection.execute(
                text(insert_query),
                {
                    "user_id": user_id,
                    "song_id": int(row['id'])
                }
            )

        connection.commit()

    print("Recommendations saved successfully!")

user_id = 1

history = get_user_history(user_id)

print("\nUser History:\n")
print(history.head())

recommendations = get_recommendations(user_id)

print("\nRecommendations:\n")
print(recommendations)

save_recommendations(user_id, recommendations)