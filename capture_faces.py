import cv2
import os

# Create dataset directory if it doesn't exist
DATASET_PATH = "dataset/"
if not os.path.exists(DATASET_PATH):
    os.makedirs(DATASET_PATH)

# Ask for user name
name = input("Enter the person's name: ")
person_folder = os.path.join(DATASET_PATH, name)

if not os.path.exists(person_folder):
    os.makedirs(person_folder)

# Open webcam
cap = cv2.VideoCapture(0)
count = 0

print("Capturing images... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Face", frame)

    # Save every 5th frame to reduce duplicates
    if count % 5 == 0:
        img_path = os.path.join(person_folder, f"{count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Saved: {img_path}")

    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
