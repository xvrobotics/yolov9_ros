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
    git clone https://github.com/xvrobotics/yolov9_ros.git
    cd yolov9_ros
    ```

2. **Install Dependencies**:
    Ensure all required dependencies are installed.
    ```bash
    cd src/yolov9/yolov9
    pip3 install -r requirements.txt
    ```

3. **Build the Package**:
    ```bash
    cd ~/yolov9_ros
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

- **`/camera/raw/image`**: Subscribes to an image topic for object detection.

### Parameters

- **`weights`**: Path to the YOLOv9 model weights.
- **`source`**: Input source for detection (`ros` for ROS topic, or other sources like file path).
- **`conf_thres`**: Minimum confidence required for a detection to be considered valid.
- **`imgsz`**: Image size used for inference.
- **`iou_thres`**: IoU threshold for non-max suppression.
- **`max_det`**: Maximum number of detections per image.
- **`device`**: Device to run inference on (`0` for GPU, `cpu` for CPU).
- **`view_img`**: Boolean flag to display the annotated image.
- **`save_txt`**: Boolean flag to save detection results as text.
- **`save_conf`**: Boolean flag to save confidence scores in the text labels.
- **`save_crop`**: Boolean flag to save cropped detection results.
- **`nosave`**: Boolean flag to prevent saving images/videos.
- **`classes`**: Filter detections by class.
- **`agnostic_nms`**: Boolean flag for class-agnostic non-max suppression.
- **`augment`**: Boolean flag for augmented inference.
- **`visualize`**: Boolean flag to visualize feature maps.
- **`update`**: Boolean flag to update all models.
- **`project`**: Directory to save results.
- **`name`**: Name of the folder to save results.
- **`exist_ok`**: Boolean flag to allow overwriting of existing project names.
- **`line_thickness`**: Thickness of bounding box lines in the annotated image.
- **`hide_labels`**: Boolean flag to hide labels in the annotated image.
- **`hide_conf`**: Boolean flag to hide confidence scores in the annotated image.
- **`half`**: Boolean flag to use FP16 half-precision inference.
- **`dnn`**: Boolean flag to use OpenCV DNN for ONNX inference.
- **`vid_stride`**: Video frame-rate stride.
- **`data`**: Path to the dataset YAML file.
- **`input_topic`**: The topic to subscribe to for incoming images. Default is `/camera/raw/image`.
- **`output_topic_image`**: The topic to publish the annotated image. Default is `/yolov9/annotated_image`.
- **`output_topic_detections`**: The topic to publish detection data. Default is `/yolov9/detections`.



## Customization

You can fine-tune the YOLOv9 model by adjusting the parameters in the `config` file. This includes modifying the confidence threshold, changing the input/output topics, and setting other detection parameters.

## Example

Here's an example of how to run the package, make sure you changed the :

```bash
ros2 launch yolov9_ros yolov9.launch.py
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
