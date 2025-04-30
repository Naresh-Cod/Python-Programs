import cv2
import mediapipe as mp
import numpy as np
import subprocess

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def set_volume_linux(volume_percent):
    # Use pactl to set volume (0 to 100)
    subprocess.call(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume_percent}%"])

def calc_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    lm_list = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if lm_list:
        x1, y1 = lm_list[4][1], lm_list[4][2]   # Thumb tip
        x2, y2 = lm_list[8][1], lm_list[8][2]   # Index tip

        cv2.circle(img, (x1, y1), 10, (255, 0, 0), -1)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), -1)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

        length = calc_distance(x1, y1, x2, y2)

        # Map length to volume percentage
        volume_percent = int(np.interp(length, [30, 200], [0, 100]))
        set_volume_linux(volume_percent)

        # Show volume bar
        bar_height = int(np.interp(length, [30, 200], [400, 150]))
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 2)
        cv2.rectangle(img, (50, bar_height), (85, 400), (0, 255, 0), -1)
        cv2.putText(img, f'{volume_percent} %', (40, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Linux Hand Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
