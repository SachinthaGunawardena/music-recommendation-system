import pandas as pd

from src.recommender.content_based import get_recommendations

# Load dataset
data = pd.read_csv(
    "data/processed/cleaned_music_dataset.csv"
)


def recommend_songs(song_name):

    recommendations = get_recommendations(song_name)

    return recommendations.to_dict(
        orient="records"
    )


def search_song(song_name):

    results = data[
        data["track_name"].str.contains(
            song_name,
            case=False,
            na=False
        )
    ][["track_name", "artist_name", "genre"]]

    return results.head(10).to_dict(
        orient="records"
    )


def top_tracks():

    tracks = data[
        ["track_name", "artist_name", "genre"]
    ].head(10)

    return tracks.to_dict(
        orient="records"
    )