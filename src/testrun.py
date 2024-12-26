import cv2
import numpy as np
from ultralytics import YOLO
import tensorflow as tf

def run_yolo_inference_yolov8(weights_path, model_type='yolo'):
    model = YOLO(weights_path)
    cap = cv2.VideoCapture(0)  # Open the camera

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        results = model.predict(frame, conf=0.5)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def run_tf_lite_inference(weights_path):
    # Load TensorFlow Lite model and allocate tensors
    interpreter = tf.lite.Interpreter(model_path=weights_path)
    interpreter.allocate_tensors()

    # Get input and output details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    cap = cv2.VideoCapture(0)  # Open the camera

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        input_shape = input_details[0]['shape'][1:3]
        resized_frame = cv2.resize(frame, (input_shape[1], input_shape[0]))
        input_data = np.expand_dims(resized_frame, axis=0).astype(np.float32) / 255.0

        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        output_data = interpreter.get_tensor(output_details[0]['index'])

        # Process output_data here for visualization if applicable
        # For simplicity, this displays the raw output as text (customize as needed)
        cv2.putText(frame, f"Output: {output_data}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("TensorFlow Lite Inference", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    model_type = input("Enter model type (yolo/tf-lite): ").strip()
    weights_path = input("Enter weights path: ").strip()

    if model_type == 'yolo':
        run_yolo_inference_yolov8(weights_path)
    elif model_type == 'tf-lite':
        run_tf_lite_inference(weights_path)
    else:
        print("Invalid model type")
