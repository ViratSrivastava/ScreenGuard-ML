from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('src\\models\\YOLOv8\\weights\\runs\\train\\baby_face_detection\\weights\\best.pt')  # Use double backslashes

# Export the model to TensorFlow SavedModel format
model.export(format='saved_model', opset=13)

import tensorflow as tf

# Path to the SavedModel directory
saved_model_dir = "src\\models\\YOLOv8\\weights\\runs\\train\\baby_face_detection\\weights\\best_saved_model"

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Optional: Optimize for size/speed
tflite_model = converter.convert()

# Save the TFLite model
with open("yolov8n.tflite", "wb") as f:
    f.write(tflite_model)

print("Model converted to TFLite format!")
