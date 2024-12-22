# Model Inference Documentation

This README provides an overview of the models, their weights, usage instructions, and observations for improvements in future datasets.

## Models and Weights

### 1. **YOLOv8 Models**
- **Model Weights**:
- **Framework**: PyTorch/Ultralytics
- **Description**: These models were trained using the YOLOv8 framework for object detection tasks.

### 2. **TensorFlow Lite Models**
- **Model Weights**:
- **Framework**: TensorFlow Lite
- **Description**: These models were optimized for edge devices and designed to detect babies.

## Usage Instructions

### Running YOLOv8 Models
1. Install dependencies:
   ```bash
   pip install ultralytics opencv-python
   ```
2. Use the provided inference script to run real-time detection via a camera.
3. Provide the weights path and execute the script.

### Running TensorFlow Lite Models
1. Install dependencies:
   ```bash
   pip install tensorflow opencv-python
   ```
2. Load the `.tflite` model using TensorFlow Lite's Interpreter API.
3. Use the inference script to process live camera feed or static images.

## Observations and Improvements

### Current Limitations
- **Dataset Limitation**: The dataset includes only babies as a class.
  - This narrow focus limits the model's applicability in real-world scenarios where adults and other entities may need to be detected alongside babies.

### Recommendations
1. **Expand Dataset Classes**:
   - Include adults and other relevant categories to enhance model utility.
   - Collect diverse data to improve robustness and real-world accuracy.
2. **Augment Dataset**:
   - Add more variations in lighting, poses, and environments to reduce overfitting to specific conditions.
3. **Model Optimization**:
   - Evaluate model performance on edge devices for real-time applications.

## Conclusion
These models demonstrate good performance for baby detection but require additional data diversity and class expansion for broader use cases. Further iterations should incorporate multi-class datasets and optimized training strategies for improved results.
