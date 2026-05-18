from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:abc123@localhost:5432/music_recommendation_db"

engine = create_engine(DATABASE_URL)

users = [
    ("john", "john@gmail.com"),
    ("emma", "emma@gmail.com"),
    ("alex", "alex@gmail.com"),
    ("sophia", "sophia@gmail.com")
]

insert_query = """
INSERT INTO users (username, email)
VALUES (:username, :email)
"""

with engine.connect() as connection:

    for username, email in users:
        connection.execute(
            text(insert_query),
            {
                "username": username,
                "email": email
            }
        )

    connection.commit()

print("Users inserted successfully!")