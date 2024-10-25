# Football Analysis System Using YOLO, OpenCV, and Python

## Project Overview
The aim of this project is to develop an automated Football Analysis System that can detect and track players, referees, and the football in a match video using advanced AI techniques. These techniques include:
- **YOLO (You Only Look Once)** for object detection
- **KMeans clustering** for t-shirt color segmentation
- **Optical Flow** to measure camera movement

The system not only tracks the movement of players but also assigns them to their respective teams and calculates key performance metrics such as ball possession, distance covered, and speed. The project simulates real-world conditions for analyzing football matches.

## Key Features
- **Player, Referee, and Football Detection**: YOLO detects and tracks these entities across video frames.
- **Team Assignment**: Players are assigned to teams based on t-shirt color using KMeans clustering.
- **Ball Possession Tracking**: Calculates ball possession percentage for each team by tracking which player has the ball.
- **Player Movement and Speed**: Optical Flow and perspective transformation are used to measure player movement in meters and calculate speed.
- **Camera Movement Compensation**: Compensates for camera movement to ensure accurate player tracking.
- **Player Identification**: Tracks special players like goalkeepers using distinct visual representations.

## Initial Input
<img width="800" alt="image" src="https://github.com/user-attachments/assets/88390adb-16b5-46b1-a741-f4537ae4f15d">

## Final Output
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/52db3c45-ab0b-4bb5-8b00-0d30e567ad09">

## Dataset Information
- **Video Dataset**: Initial video data was sourced from the [DFL - Bundesliga Data Shootout on Kaggle](https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout).
- **Training Dataset**: The training images used for object detection were sourced from [Roboflow's Football Players Detection Dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1).

## Modules Used
- **YOLOv8x**: Used for object detection to track players, referees, and football.
- **KMeans Clustering**: For segmenting the player t-shirts based on colors to assign team labels.
- **Optical Flow**: To calculate and compensate for camera movement.
- **Perspective Transformation**: Represents depth and perspective, enabling accurate measurement of player movement in meters.
- **Ultralytics YOLOv8x**: Chosen for high accuracy in object detection and large model parameters.

## Step-by-Step Project Implementation

### Step 1: Initial Setup and Data Preparation
- The initial video dataset was sourced from Kaggle, while a football player image dataset from Roboflow was used for training YOLO.
- YOLOv8x was employed for initial object detectiondue to its large number of parameters, offering higher accuracy but demanding significant computational resources.

### Step 2: Object Detection and Bounding Box Creation
- YOLO detected players, football, and referees with bounding box coordinates providing their bounding box coordinates (x, y, w, h) and confidence scores.
- Initial challenges:
  - Irregular football detection.
  - Detection of people outside the field.
  - Referees being classified as players.

### Step 3: Model Training (YOLOv5x)
- Retrained YOLOv5x to improve detection accuracy.
- Training Command:
    ```bash
    !yolo task=detect mode=train model=yolov5x.pt data={dataset.location}/data.yaml epochs=100 imgsz=640
    ```
- Training Time: 78 hours
- Output Files:
  - `best.pt` (best performing weights)
  - `worst.pt`

### Step 4: Team Assignment Using KMeans Clustering
- Segmented and clustered pixels from player bounding boxes to assign teams based on their t-shirt colors using KMeans Clustering.
     ![image](https://github.com/user-attachments/assets/a299b616-8274-4ab0-9304-6d7987d14619)

### Step 5: Ball Tracking and Ball Acquisition
- A custom method was created to predict the ball’s position between frames based on their trajectory.
- Ball possession was calculated by assigning the closest player to the ball.

### Step 6: Camera Movement and Optical Flow
- Optical Flow techniques were used to detect camera movement and compensate for camera motion and ensure accurate tracking of player movements.

### Step 7: Perspective Transformation
- Applied perspective transformation to convert pixel movements into real-world distances (in meters), allowing us to measure the actual distance covered by each player.

### Step 8: Speed and Distance Calculation
- Speed and distance covered by players during the game were calculated.

### Step 9: Special Player Tracking
- Goalkeepers were tracked separately using unique color code(yellow ellipses) and visual markers.

## Key Improvements from Initial Detection
- Improved football detection with YOLOv5x, football detection accuracy increased significantly.
- Non-field objects (people outside the field) were excluded from detection.
- Referees were correctly identified and differentiated from players using distinct markers.

## Final Training Results
After completing the model training, the system accurately detected key elements on the football field, including the ball, players, referees, and goalkeepers. The model's performance was tested on a video file, yielding highly accurate results. The detected objects included several players and referees with high confidence scores.
Below are some key detection results:

- **Detections**:
  - Class labels: ball (0), goalkeeper (1), player (2), referee (3)
  - Inference Speed: Preprocessing took 2.73 ms, inference 284.92 ms, and post-processing 5.13 ms.

- **Player Detection**:
    - Confidence: 94.01%, Bounding Box: (852.2585, 633.0989, 901.4484, 720.9474)
    - Confidence: 93.14%, Bounding Box: (1309.8802, 447.5838, 1351.0917, 516.6583)
    - Confidence: 92.38%, Bounding Box: (995.5633, 453.6966, 1027.6948, 526.1847)

- **Referee Detection**:
    - Confidence: 92.16%, Bounding Box: (1853.5166, 808.6301, 1894.2949, 918.1991)

- **Goalkeeper Detection**:
    - Confidence: 88.41%, Bounding Box: (1901.8114, 374.9146, 1919.9996, 442.5521)

- **Ball Detection**:
    - Confidence: 89.48%, Bounding Box: (1161.3645, 354.8108, 1187.4310, 412.2182)

## Input and Output of Project
[Input Video](https://drive.google.com/file/d/1sW3GNXyPfWy3r1oJk5nijlGuY7BYsz_t/view?usp=sharing)

[Final Output](https://drive.google.com/file/d/1B1gHIw6b1eEuMz6bp054eGGIkLsqBdl8/view?usp=sharing)

## Conclusion
The football analysis model demonstrates high accuracy, with confidence scores exceeding 90% for most detected objects. The system’s detection accuracy and inference speed make it a reliable tool for further football analytics tasks, including player tracking and tactical analysis.
These results highlight the effectiveness of the training process and demonstrate that the model is ready for deployment in real-time football analytics applications.
