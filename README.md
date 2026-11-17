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
[<img width="599" height="454" alt="vehicle detection" src="https://github.com/user-attachments/assets/0426ef9f-f494-45d6-9731-23e1361e8424" />
](<img width="599" height="454" alt="vehicle detection" src="https://github.com/user-attachments/assets/5240d50f-7f0e-4a9a-a0e2-0bc08d31b4f3" />
)

### Multiple Vehicle Detection
[<img width="592" height="414" alt="multiple cars" src="https://github.com/user-attachments/assets/d821753b-3acc-4047-8c59-1216e8e449ec" />
](<img width="592" height="414" alt="multiple cars" src="https://github.com/user-attachments/assets/d821753b-3acc-4047-8c59-1216e8e449ec" />
)

### Vehicle Counting
[<img width="590" height="358" alt="vehicles count" src="https://github.com/user-attachments/assets/1955878b-f7d9-41a4-9ef6-5fbd5f60e8a4" />
](<img width="590" height="358" alt="vehicles count" src="https://github.com/user-attachments/assets/d22c10e6-d97d-446a-872d-7a2fb4fef7b6" />
)


## Project Outcome

The project demonstrates the application of pre-trained object detection models and computer vision techniques for vehicle identification and counting. It provided practical experience in object detection, image processing, object tracking and the development of a real-time machine learning application.

## Author

**Abhishek**

[GitHub Profile](https://github.com/Abhishek-2709)
