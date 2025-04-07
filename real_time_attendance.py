import cv2
import face_recognition
import pickle
from datetime import datetime

# Load trained model
with open("models/face_encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_face_encodings = data["encodings"]
known_face_names = data["names"]

# Initialize webcam
video_capture = cv2.VideoCapture(0)

attendance_log = {}

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]

            # Mark attendance
            if name not in attendance_log:
                attendance_log[name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Attendance marked: {name} at {attendance_log[name]}")

        # Draw a rectangle around recognized faces
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
