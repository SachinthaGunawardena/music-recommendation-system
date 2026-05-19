from sqlalchemy import create_engine, text
import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

indexes_query = """

CREATE INDEX IF NOT EXISTS idx_history_user
ON listening_history(user_id);

CREATE INDEX IF NOT EXISTS idx_history_song
ON listening_history(song_id);

CREATE INDEX IF NOT EXISTS idx_recommendations_user
ON recommendations(user_id);

CREATE INDEX IF NOT EXISTS idx_recommendations_song
ON recommendations(song_id);

"""

with engine.connect() as connection:

    connection.execute(text(indexes_query))

    connection.commit()

print("Indexes created successfully!")