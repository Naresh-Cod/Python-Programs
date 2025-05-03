import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

user_id = input("Enter user ID: ")
os.makedirs(f"faces/{user_id}", exist_ok=True)

count = 0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face_img = gray[y:y+h, x:x+w]
        cv2.imwrite(f"faces/{user_id}/{count}.jpg", face_img)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Capturing Faces", frame)
    if cv2.waitKey(1) == 27 or count >= 50:  # ESC to stop
        break

cap.release()
cv2.destroyAllWindows()
