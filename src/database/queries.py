import pandas as pd
from sqlalchemy import create_engine

import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM songs LIMIT 10"

df = pd.read_sql(query, engine)

print(df)