import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

# Load dataset
df = pd.read_csv("data/raw/tcc_ceds_music.csv")

# Select columns
songs_df = df[['track_name', 'artist_name', 'genre', 'release_date']]

# Insert into PostgreSQL
songs_df.to_sql(
    "songs",
    engine,
    if_exists="append",
    index=False
)

print("Dataset inserted successfully!")