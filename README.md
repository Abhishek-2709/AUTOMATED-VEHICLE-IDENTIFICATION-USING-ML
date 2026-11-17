## Automated Vehicle Identification Using Machine Learning

## Project Overview

This project explores machine learning and computer vision for automated vehicle identification and traffic monitoring. It uses the YOLOv4-tiny object detection model to identify and classify vehicles from video input.

The system detects vehicle categories such as cars, motorcycles, buses and trucks, while incorporating tracking logic to avoid repeatedly counting the same vehicle across consecutive frames.

## Problem Statement

Manual vehicle monitoring can be time-consuming, particularly in areas with continuous traffic flow. Automated vehicle detection and classification provide an efficient approach to analysing traffic and collecting vehicle-related information.

This project addresses this problem by combining object detection, image processing and basic object tracking techniques.

## Technical Approach

The system follows a computer vision-based workflow:

1. **Input:** Captures video through a webcam.
2. **Preprocessing:** Processes video frames using OpenCV.
3. **Detection:** Uses the YOLOv4-tiny model to identify objects in each frame.
4. **Classification:** Identifies vehicle categories, including cars, motorcycles, buses and trucks.
5. **Tracking:** Uses bounding-box overlap to identify previously detected vehicles and reduce duplicate counting.
6. **Counting:** Maintains vehicle counts by category.
7. **Visualisation:** Displays detection results and vehicle counts on the video frames.

## Key Technologies

- **Python** – Application development
- **YOLOv4-tiny** – Object detection
- **OpenCV** – Image and video processing
- **NumPy** – Numerical operations
- **COCO Dataset Classes** – Object category identification

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/Abhishek-2709/AUTOMATED-VEHICLE-IDENTIFICATION-USING-ML.git
```

### 2. Navigate to the project directory

```bash
cd AUTOMATED-VEHICLE-IDENTIFICATION-USING-ML
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download required model files

```bash
python download_models.py
```

This script downloads the required YOLOv4-tiny configuration, model weights and COCO class names when they are missing.

### 5. Run the application

```bash
python vehicle_detector.py
```

Make sure your webcam is connected and camera access is enabled.


## Screenshots

### Vehicle Detection
![Vehicle Detection](screenshots/vehicle-detection.png)

### Multiple Vehicle Detection
![Multiple Vehicle Detection](screenshots/multiple-vehicles.png)

### Vehicle Counting
![Vehicle Counting](screenshots/vehicle-counting.png)


## Project Outcome

The project demonstrates the application of pre-trained object detection models and computer vision techniques for vehicle identification and counting. It provided practical experience in object detection, image processing, object tracking and the development of a real-time machine learning application.

## Author

**Abhishek**

[GitHub Profile](https://github.com/Abhishek-2709)