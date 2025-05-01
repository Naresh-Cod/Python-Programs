import cv2
import mediapipe as mp
import time
import math

# Mediapipe initialization
mp_face = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face.FaceDetection(model_selection=1, min_detection_confidence=0.5)
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)
photo_taken = False

def is_ok_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    dist = math.hypot(thumb_tip.x - index_tip.x, thumb_tip.y - index_tip.y)
    return dist < 0.05  # You can adjust threshold based on camera

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect face and hands
    face_results = face_detection.process(image_rgb)
    hand_results = hands.process(image_rgb)

    # Check for smile (proxy: face detected)
    is_smiling = face_results.detections is not None

    # Check for OK hand sign
    ok_detected = False
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            if is_ok_sign(hand_landmarks):
                ok_detected = True
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # If both detected, save photo once
    if is_smiling and ok_detected and not photo_taken:
        filename = f'smile_ok_photo_{int(time.time())}.jpg'
        cv2.imwrite(filename, image)
        print(f"[✓] Photo saved: {filename}")
        photo_taken = True  # Save only once

    # Draw face detection
    if face_results.detections:
        for detection in face_results.detections:
            mp_drawing.draw_detection(image, detection)

    cv2.imshow('Smile + OK Gesture Detector', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
