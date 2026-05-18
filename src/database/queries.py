import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM songs LIMIT 10"

df = pd.read_sql(query, engine)

print(df)