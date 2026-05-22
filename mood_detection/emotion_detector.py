
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import cv2
from fer import FER
from collections import Counter


# Initialize FER detector
detector = FER(mtcnn=True)

def detect_emotion():

    cap = cv2.VideoCapture(0)

    detected_emotions = []

    # Read multiple frames
    for _ in range(15):

        ret, frame = cap.read()

        if not ret:
            continue

        # Detect emotions
        emotions = detector.detect_emotions(frame)

        if emotions:

            emotion_scores = emotions[0]["emotions"]

            # Best emotion
            detected_emotion = max(
                emotion_scores,
                key=emotion_scores.get
            )

            confidence = emotion_scores[detected_emotion]

            # Ignore weak predictions
            if confidence > 0.40:

                detected_emotions.append(detected_emotion)

    cap.release()

    # If nothing detected
    if not detected_emotions:
        return "neutral"

    # Most common emotion
    final_emotion = Counter(
        detected_emotions
    ).most_common(1)[0][0]

    return final_emotion