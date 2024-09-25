'''
Age-gender network: https://github.com/opencv/opencv/tree/master/samples/dnn/face_detector
You'll need the .prototxt and .caffemodel files for both face detection and age-gender recognition
`To use this script:

Download the model files:

For face detection:
deploy.prototxt
res10_300x300_ssd_iter_140000.caffemodel
For age-gender recognition:
age_deploy.prototxt
age_net.caffemodel
Place these files in the same directory as your script or update the file paths in the cv2.dnn.readNet() calls.
Run the script.


 https://www.blackbox.ai/share/54085208-eacd-4adc-9c47-a19731a8c9a8?model=claude-sonnet-3.5
'''

import cv2
import numpy as np

#Load face detection model
face_net = cv2.dnn.readNet("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")

# Load age-gender recognition model
age_net = cv2.dnn.readNet("age_deploy.prototxt", "age_net.caffemodel")

# Define age buckets
age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam or provide video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    # Prepare input blob for face detection
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    
    # Set input for face detection
    face_net.setInput(blob)
    
    # Forward pass through the network
    face_detections = face_net.forward()

    for i in range(face_detections.shape[2]):
        confidence = face_detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            box = face_detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x, y, x2, y2) = box.astype("int")
            
            # Extract face ROI
            face_roi = frame[y:y2, x:x2]

            # Prepare input blob for age-gender recognition
            blob = cv2.dnn.blobFromImage(face_roi, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

            # Set input for age-gender recognition
            age_net.setInput(blob)
            
            # Forward pass through the network
            age_preds = age_net.forward()
            age = age_list[age_preds[0].argmax()]

            # Draw bounding box and age
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()