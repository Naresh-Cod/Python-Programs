import cv2
import mediapipe as mp

# Initialize Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Capture video
cap = cv2.VideoCapture(0)

# Hand tracking model
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# For drawing line
prev_x, prev_y = 0, 0
canvas = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for natural interaction
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Create canvas to draw on
    if canvas is None:
        canvas = frame.copy()

    # Convert to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Index finger tip
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            # Draw line from previous point to current
            cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 0, 255), 5)
            prev_x, prev_y = x, y

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    else:
        # Reset if hand not detected
        prev_x, prev_y = 0, 0

    # Merge canvas and camera frame
    combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    cv2.imshow("Hand Tracker with Drawing", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
