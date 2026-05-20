import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import HTTPException

# Load dataset
data = pd.read_csv("data/enhanced_music.csv")

# Create combined features
data["combined_features"] = (
    data["genre"].fillna('') + " " +
    data["artist_name"].fillna('') + " " +
    data["track_name"].fillna('')
)

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(data["combined_features"])

# Similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix)

def get_recommendations(song_title, top_n=10):

    idx = data[data["track_name"] == song_title].index
    
    if len(idx) == 0:
        raise HTTPException(
        status_code=404,
        detail="Song not found"
    )

    idx = idx[0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:top_n+1]

    song_indices = [i[0] for i in sim_scores]

    recommendations = data.iloc[song_indices][
        ["track_name", "artist_name", "genre"]
    ]

    return recommendations.to_dict(orient="records")

def recommend_songs_by_genre(genre, top_n=5):

    # Filter songs by genre
    filtered_songs = data[
        data["genre"].str.lower() == genre.lower()
    ]

    # Check if empty
    if filtered_songs.empty:
        return []

    # Select columns
    recommendations = filtered_songs[
        ["track_name", "artist_name", "genre"]
    ].head(top_n)

    # Convert to dictionary
    return recommendations.to_dict(orient="records")