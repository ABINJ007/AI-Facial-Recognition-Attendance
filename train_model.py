import face_recognition
import pickle
import os
import cv2

DATASET_PATH = "dataset/"
MODEL_PATH = "models/face_encodings.pkl"

known_face_encodings = []
known_face_names = []

for person in os.listdir(DATASET_PATH):
    person_folder = os.path.join(DATASET_PATH, person)

    if os.path.isdir(person_folder):
        for filename in os.listdir(person_folder):
            image_path = os.path.join(person_folder, filename)
            image = face_recognition.load_image_file(image_path)
            
            face_encoding = face_recognition.face_encodings(image)
            if face_encoding:
                known_face_encodings.append(face_encoding[0])
                known_face_names.append(person)

# Save encodings to a file
data = {"encodings": known_face_encodings, "names": known_face_names}
with open(MODEL_PATH, "wb") as f:
    f.write(pickle.dumps(data))

print("Face encoding complete and saved!")
