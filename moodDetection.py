import cv2
import math
import time
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces


def filter_faces(faces, frame_width, frame_height):
    center_x = frame_width // 2
    center_y = frame_height // 2
    closest_face = None
    min_distance = float('inf')
    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        distance = math.sqrt((center_x - face_center_x) ** 2 + (center_y - face_center_y) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_face = (x, y, w, h)
    return [closest_face] if closest_face is not None else []


def mood ():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    mood_estimations = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_height, frame_width, _ = frame.shape
        faces = detect_faces(frame)

        filtered_faces = filter_faces(faces, frame_width, frame_height)
        for (x, y, w, h) in filtered_faces:
            face_img = frame[y:y+h, x:x+w]
            result = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
            emotions = result[0]['emotion']
            mood_estimations.append(emotions)
            cv2.putText(frame, "Mood: Analyzing...", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Mood Detection', frame)

        if time.time() - start_time >= 5:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if mood_estimations:
        total_estimations = len(mood_estimations)
        mood_sum = {}
        for mood in mood_estimations:
            for emotion, value in mood.items():
                mood_sum[emotion] = mood_sum.get(emotion, 0) + value
        dominant_mood = max(mood_sum, key=mood_sum.get)
        return dominant_mood