import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

try:

    connection = engine.connect()

    print("Database connected successfully!")

    connection.close()

except Exception as e:

    print("Connection failed!")

    print(e)