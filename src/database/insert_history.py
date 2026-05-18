from sqlalchemy import create_engine, text
import random

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

# Simulated listening history
history_data = []

# Create random listening activity
for _ in range(100):

    user_id = random.randint(1, 4)

    song_id = random.randint(1, 100)

    history_data.append(
        {
            "user_id": user_id,
            "song_id": song_id
        }
    )

insert_query = """
INSERT INTO listening_history (user_id, song_id)
VALUES (:user_id, :song_id)
"""

with engine.connect() as connection:

    for record in history_data:

        connection.execute(
            text(insert_query),
            record
        )

    connection.commit()

print("Listening history inserted successfully!")