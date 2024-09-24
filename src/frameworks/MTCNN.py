import cv2
import numpy as np
from mtcnn import MTCNN
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load pre-trained models
face_detector = MTCNN()
age_model = load_model('weights\MTCNN\MTCNN_model.h5')

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam or provide video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect faces
    faces = face_detector.detect_faces(frame)

    for face in faces:
        x, y, width, height = face['box']
        
        # Extract face ROI
        face_roi = frame[y:y+height, x:x+width]
        
        # Preprocess for age estimation
        face_roi = cv2.resize(face_roi, (64, 64))
        face_roi = face_roi.astype("float") / 255.0
        face_roi = img_to_array(face_roi)
        face_roi = np.expand_dims(face_roi, axis=0)
        
        # Predict age
        age_pred = age_model.predict(face_roi)[0][0]
        age = int(age_pred)
        
        # Draw bounding box and age
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)
        cv2.putText(frame, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()