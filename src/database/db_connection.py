from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Database connected successfully!")
    connection.close()

except Exception as e:
    print("Connection failed!")
    print(e)