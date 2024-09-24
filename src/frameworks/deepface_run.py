import cv2
import numpy as np
from mtcnn import MTCNN
from deepface import DeepFace

# Initialize face detector
face_detector = MTCNN()

def get_available_camera():
    for i in range(10):  # Check first 10 indexes
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera found at index {i}")
            return cap
    print("No camera found")
    return None

# Initialize video capture
cap = get_available_camera()

if cap is None:
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Detect faces
        faces = face_detector.detect_faces(frame)

        for face in faces:
            x, y, width, height = face['box']
            
            # Extract face ROI
            face_roi = frame[y:y+height, x:x+width]
            
            try:
                # Predict age using DeepFace
                result = DeepFace.analyze(face_roi, actions=['age'], enforce_detection=False, detector_backend='opencv')
                age = result[0]['age']
                
                # Draw bounding box and age
                cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)
                cv2.putText(frame, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            except Exception as e:
                print(f"Error in age estimation: {str(e)}")

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()