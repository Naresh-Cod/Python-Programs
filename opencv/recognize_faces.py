import cv2
import numpy as np
import os

# Prepare training data
def prepare_data(data_folder_path):
    faces = []
    labels = []
    label_map = {}

    for idx, person in enumerate(os.listdir(data_folder_path)):
        person_folder = os.path.join(data_folder_path, person)
        label_map[idx] = person

        for img_name in os.listdir(person_folder):
            img_path = os.path.join(person_folder, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            labels.append(idx)

    return faces, labels, label_map

faces, labels, label_map = prepare_data("faces")

# Train recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))

# Start recognition
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_detected = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces_detected:
        roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi)
        name = label_map.get(label, "Unknown")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({round(confidence, 2)})", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
