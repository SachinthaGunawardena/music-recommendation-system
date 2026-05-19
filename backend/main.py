from fastapi import FastAPI
from backend.recommender import get_recommendations

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Music Recommendation API is running"}


from typing import List
from backend.schemas import SongResponse


from fastapi import HTTPException


@app.get(
    "/recommend/{song_name}",
    response_model=List[SongResponse]
)
def recommend(song_name: str):

    recommendations = get_recommendations(song_name)

    return recommendations


from backend.recommender import data


@app.get("/search/{query}")
def search_song(query: str):

    results = data[
        data["track_name"].str.contains(query, case=False)
    ][["track_name", "artist_name", "genre"]].head(10)

    return results.to_dict(orient="records")
