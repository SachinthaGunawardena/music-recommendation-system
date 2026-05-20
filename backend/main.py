from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

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