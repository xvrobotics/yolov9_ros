# YOLOv9_ROS

## Overview

`yolov9_ros` is a ROS2 package that integrates YOLOv9 object detection with ROS2 Humble. It allows for real-time object detection using a ROS2 topic image as input. The package processes the image to detect objects based on a pre-trained YOLOv9 model and publishes the results, including an annotated image with bounding boxes and a ROS2 topic containing detailed object detection information such as bounding box coordinates, confidence scores, and object labels.

## Features

- **YOLOv9 Integration**: Leverages the YOLOv9 deep learning model for fast and accurate object detection.
- **ROS2 Compatibility**: Built specifically for ROS2 Humble, ensuring seamless integration with other ROS2 nodes and tools.
- **Real-time Detection**: Processes incoming images from a ROS2 topic and publishes detection results in real-time.
- **Detailed Detection Outputs**:
  - Annotated image with bounding boxes.
  - ROS2 topic with bounding box pixel coordinates, confidence scores, and object labels.
  
## Installation

### Prerequisites

- ROS2 Humble
- Python 3.8+
- OpenCV
- PyTorch
- YOLOv9 model weights

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/yolov9_ros.git
    cd yolov9_ros
    ```

2. **Install Dependencies**:
    Ensure all required dependencies are installed.
    ```bash
    pip install -r requirements.txt
    ```

3. **Build the Package**:
    ```bash
    colcon build
    ```

4. **Source the Setup Script**:
    ```bash
    source install/setup.bash
    ```

## Usage

### Launching the Node

To start the YOLOv9 detection node, run the following command:

```bash
ros2 launch yolov9_ros yolov9.launch.py
```
### Published Topics

- **`/yolov9/detections`**: Publishes a custom message containing:
  - Bounding box pixel coordinates
  - Confidence scores
  - Object labels
- **`/yolov9/annotated_image`**: Publishes an image with bounding boxes drawn around detected objects.

### Subscribed Topics

- **`/input_image`**: Subscribes to an image topic for object detection.

### Parameters

- **`model_path`**: Path to the YOLOv9 model weights.
- **`confidence_threshold`**: Minimum confidence required for a detection to be considered valid.
- **`input_topic`**: The topic to subscribe to for incoming images.
- **`output_topic_image`**: The topic to publish the annotated image.
- **`output_topic_detections`**: The topic to publish detection data.

## Customization

You can fine-tune the YOLOv9 model by adjusting the parameters in the `config` file. This includes modifying the confidence threshold, changing the input/output topics, and setting other detection parameters.

## Example

Here's an example of how to run the package:

```bash
ros2 launch yolov9_ros yolov9.launch.py input_topic:=/camera/image_raw output_topic_image:=/yolov9/annotated_image output_topic_detections:=/yolov9/detections
```
## Citation

If you use this package in your research or project, please consider citing it as follows:

```bash
@misc{XavierVicent2024yolov9ros,
  author = {Xavier Vicent},
  title = {{yolov9_ros}: A ROS2 Package for YOLOv9 Object Detection},
  year = {2024},
  howpublished = {\url{https://github.com/xvrobotics/yolov9_ros}},
}
```
## Contributing

Contributions are welcome! If you'd like to contribute to this project, please feel free to submit a pull request or open an issue.

## Contact

For any questions, suggestions, or feedback, please contact [Xavier Vicent](mailto:xvicentnavar2024@fau.edu).
