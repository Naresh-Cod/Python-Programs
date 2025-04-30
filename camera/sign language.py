import cv2
import mediapipe as mp
import tensorflow as tf
import numpy as np
import os
import time
from collections import deque


class SignLanguageRecognizer:
    def __init__(self):
        # Mediapipe setup
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils

        # Load trained model
        self.model_path = "/home/kalikali/Documents/python/sign_language_model.h5"
        if not os.path.isfile(self.model_path):
            raise FileNotFoundError(f"Model file '{self.model_path}' not found.")
        self.model = tf.keras.models.load_model(self.model_path)

        self.expected_input_size = self.model.input_shape[1]

        # Setup task from A to Z
        self.tasks = {chr(i): f"Show letter {chr(i)}" for i in range(65, 91)}  # A-Z
        self.current_task = 'A'
        self.task_start_time = time.time()
        self.task_time_limit = 10
        self.correct_count = 0
        self.total_tasks = 0
        self.prediction_history = deque(maxlen=5)

        # Colors
        self.COLOR_CORRECT = (0, 255, 0)
        self.COLOR_WRONG = (0, 0, 255)
        self.COLOR_TASK = (255, 255, 0)
        self.COLOR_INFO = (255, 255, 255)

    def extract_landmarks(self, hand_landmarks, width, height):
        try:
            if self.expected_input_size == 42:
                landmarks = np.array([[lm.x * width, lm.y * height] for lm in hand_landmarks.landmark])
            elif self.expected_input_size == 63:
                landmarks = np.array([[lm.x * width, lm.y * height, lm.z * 1000] for lm in hand_landmarks.landmark])
            else:
                raise ValueError(f"Unsupported model input shape: {self.expected_input_size}")

            landmarks = landmarks.flatten()
            max_val = np.max(np.abs(landmarks))
            if max_val != 0:
                landmarks = landmarks / max_val
            return landmarks
        except Exception as e:
            print(f"[ERROR] Landmark extraction failed: {e}")
            return None

    def predict_letter(self, landmarks):
        try:
            if landmarks is not None and landmarks.shape[0] == self.expected_input_size:
                prediction = self.model.predict(np.array([landmarks]), verbose=0)
                predicted_class = np.argmax(prediction)
                return chr(65 + predicted_class)  # A-Z
        except Exception as e:
            print(f"[ERROR] Prediction error: {e}")
        return None

    def update_task(self):
        if time.time() - self.task_start_time > self.task_time_limit:
            self.current_task = chr(ord(self.current_task) + 1) if self.current_task < 'Z' else 'A'
            self.task_start_time = time.time()
            self.total_tasks += 1
            self.prediction_history.clear()

    def check_task_completion(self, predicted_letter):
        if predicted_letter == self.current_task:
            self.prediction_history.append(True)
            if len(self.prediction_history) == 5 and all(self.prediction_history):
                self.correct_count += 1
                self.prediction_history.clear()
                return True
        else:
            self.prediction_history.append(False)
        return False

    def display_info(self, frame, predicted_letter):
        h, w = frame.shape[:2]
        cv2.putText(frame, f"Task: {self.tasks[self.current_task]}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, self.COLOR_TASK, 2)

        time_left = max(0, self.task_time_limit - (time.time() - self.task_start_time))
        cv2.putText(frame, f"Time: {time_left:.1f}s", (w - 160, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, self.COLOR_INFO, 2)

        if predicted_letter:
            color = self.COLOR_CORRECT if predicted_letter == self.current_task else self.COLOR_WRONG
            cv2.putText(frame, f"Showing: {predicted_letter}", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        score_text = f"Score: {self.correct_count}"
        if self.total_tasks > 0:
            score_text += f"/{self.total_tasks} ({self.correct_count / self.total_tasks:.0%})"
        cv2.putText(frame, score_text, (10, h - 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, self.COLOR_INFO, 2)

        cv2.putText(frame, "Created by Saumya", (10, h - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, self.COLOR_INFO, 1)

    def run(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Cannot access the camera.")

        print("[INFO] Webcam started. Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to grab frame.")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)
            h, w, _ = frame.shape

            self.update_task()
            predicted_letter = None

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                    landmarks = self.extract_landmarks(hand_landmarks, w, h)
                    predicted_letter = self.predict_letter(landmarks)
                    self.check_task_completion(predicted_letter)

            self.display_info(frame, predicted_letter)
            cv2.imshow("Sign Language Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        print(f"\nFinal Score: {self.correct_count}/{self.total_tasks} correct!")


if __name__ == "__main__":
    try:
        recognizer = SignLanguageRecognizer()
        recognizer.run()
    except Exception as e:
        print(f"[ERROR] {e}")
