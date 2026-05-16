from fastapi import APIRouter

from app.services.recommender_service import (
    recommend_songs,
    search_song,
    top_tracks
)

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Music Recommendation API Running"}


@router.get("/recommend/{song_name}")
def recommend(song_name: str):

    recommendations = recommend_songs(song_name)

    return {
        "song": song_name,
        "recommendations": recommendations
    }


@router.get("/search_song/{song_name}")
def search(song_name: str):

    results = search_song(song_name)

    return {
        "results": results
    }


@router.get("/top_tracks")
def get_top_tracks():

    tracks = top_tracks()

    return {
        "top_tracks": tracks
    }