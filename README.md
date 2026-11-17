# Automated Vehicle Identification Using Machine Learning

## Project Overview

This project explores the use of machine learning and computer vision for automated vehicle identification and traffic monitoring. It focuses on detecting and classifying vehicles from visual input, reducing the need for manual observation and making vehicle monitoring more efficient.

The system uses the YOLOv4-tiny object detection model to identify vehicle categories such as cars, motorcycles, buses and trucks. OpenCV is used for image processing and handling video input.

## Problem Statement

Monitoring vehicles manually can be time-consuming, particularly in areas with continuous traffic flow. Automating vehicle detection and classification provides a more efficient way to analyse traffic and collect vehicle-related information.

This project addresses that problem by combining object detection and image processing techniques in a single application.

## Technical Approach

The project follows a computer vision-based detection workflow:

1. **Input:** Captures visual data through a video source.
2. **Preprocessing:** Processes video frames using OpenCV.
3. **Detection:** Applies the YOLOv4-tiny model to identify objects in each frame.
4. **Classification:** Recognises vehicle categories, including cars, motorcycles, buses and trucks.
5. **Visualisation:** Displays detection results through annotated video frames.

## Key Technologies

- **Python** – Application development
- **YOLOv4-tiny** – Object detection
- **OpenCV** – Image and video processing
- **NumPy** – Numerical operations
- **COCO Dataset Classes** – Object category identification

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Abhishek-2709/AUTOMATED-VEHICLE-IDENTIFICATION-USING-ML.git
```

Navigate to the project directory:

```bash
cd AUTOMATED-VEHICLE-IDENTIFICATION-USING-ML
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the required model files and configure the COCO class names before running the application.


## Screenshots

### Vehicle Detection
![Vehicle Detection](screenshots/vehicle-detection.png)

### Multiple Vehicle Detection
![Multiple Vehicle Detection](screenshots/multiple-vehicles.png)

### Vehicle Counting
![Vehicle Counting](screenshots/vehicle-counting.png)


## Project Outcome

The project demonstrates how pre-trained object detection models and computer vision techniques can be combined to identify different vehicle categories from visual input. It provided practical exposure to object detection, image processing and the application of machine learning in intelligent transportation systems.

## Author

**Abhishek**

[GitHub Profile](https://github.com/Abhishek-2709)
