import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

import cv2
from fer import FER
from mood_music_mapper import mood_to_genre
from backend.recommender import recommend_songs_by_genre

# Initialize FER without MTCNN
detector = FER(mtcnn=False)

# Open webcam
cap = cv2.VideoCapture(0)

# Check camera
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:

    # Read frame
    ret, frame = cap.read()

    # Check frame
    if not ret:
        print("Failed to grab frame")
        break

    # Detect emotions
    emotions = detector.detect_emotions(frame)

    # If face detected
    if emotions:

        # Emotion scores
        emotion_scores = emotions[0]["emotions"]

        # Highest emotion
        detected_emotion = max(
            emotion_scores,
            key=emotion_scores.get
        )

        # Convert mood to genre
        recommended_genre = mood_to_genre.get(
            detected_emotion,
            "pop"
        )

        recommended_songs = recommend_songs_by_genre(
    recommended_genre
)
        print("\nDetected Mood:", detected_emotion)
        print("Recommended Genre:", recommended_genre)

        print("\nRecommended Songs:")

        for song in recommended_songs:
            print(
        f"{song['track_name']} - "
        f"{song['artist_name']}"
    )

        print("Detected Mood:", detected_emotion)
        print("Recommended Genre:", recommended_genre)

        # Draw mood text
        cv2.putText(
            frame,
            f"Mood: {detected_emotion}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Draw genre text
        cv2.putText(
            frame,
            f"Genre: {recommended_genre}",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

    # Show frame
    cv2.imshow("Mood Detection AI", frame)

    # Quit on q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()