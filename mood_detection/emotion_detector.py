import cv2
from fer import FER

# Initialize FER detector
detector = FER(mtcnn=False)

def detect_emotion():

    # Open webcam
    cap = cv2.VideoCapture(0)

    # Capture one frame
    ret, frame = cap.read()

    # Release webcam
    cap.release()

    # If failed
    if not ret:
        return "neutral"

    # Detect emotions
    emotions = detector.detect_emotions(frame)

    # If face found
    if emotions:

        emotion_scores = emotions[0]["emotions"]

        detected_emotion = max(
            emotion_scores,
            key=emotion_scores.get
        )

        return detected_emotion

    return "neutral"