from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from mood_detection.emotion_detector import detect_emotion
from backend.recommender import recommend_songs_by_genre
from mood_detection.mood_music_mapper import mood_to_genre


app = FastAPI()

# ENABLE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LOAD DATASET
data = pd.read_csv("./data/enhanced_music.csv")

print(data["genre"].unique())

# HOME
@app.get("/")
def home():
    return {"message": "Music Recommendation API"}

# RECOMMEND API
@app.get("/recommend/{song_name}")
def recommend(song_name: str):

    recommendations = data[
        data["track_name"].str.contains(song_name, case=False, na=False)
    ].head(10)

    results = []

    for _, row in recommendations.iterrows():
        results.append({
            "track_name": str(row["track_name"]),
            "artist_name": str(row["artist_name"]),
            "genre": str(row["genre"])
        })

    return {
        "recommendations": results
    }

@app.get("/detect_mood")
def detect_mood():

    mood = detect_emotion()

    return {
        "mood": mood
    }

from mood_detection.mood_music_mapper import mood_to_genre

@app.get("/mood_recommendations")
def mood_recommendations():

    mood = detect_emotion()

    genre = mood_to_genre.get(mood, "pop")

    recommendations = data[
        data["genre"].str.contains(
            genre,
            case=False,
            na=False
        )
    ].head(10)

    results = []

    for _, row in recommendations.iterrows():

        results.append({
            "track_name": str(row["track_name"]),
            "artist_name": str(row["artist_name"]),
            "genre": str(row["genre"])
        })

    return {
        "mood": mood,
        "genre": genre,
        "recommendations": results
    }

