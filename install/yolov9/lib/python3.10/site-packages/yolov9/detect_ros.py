#!/usr/bin/env python3
# YOLOv9 ROS2 Node
# Created by: Xavier Vicent
# Email: xvicentnavar2024@fau.edu
# Description: This script integrates YOLOv9 object detection with ROS2 Humble,
#              subscribing to image topics, performing object detection, and
#              publishing annotated images and detection data.
#              If you use or reference this code, please give appropriate credit.

import rclpy
from rclpy.node import Node
import numpy as np
import argparse
import os
import platform
import sys
from pathlib import Path
import torch
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
from vision_msgs.msg import Detection2D, BoundingBox2D, ObjectHypothesisWithPose
from geometry_msgs.msg import Pose2D
from yolov9_msgs.msg import YoloDetection


# Set up the file paths dynamically
FILE = Path(__file__).resolve()
ROOT = Path.home() / 'yolov9_ros/src/yolov9/yolov9'  # Direct path to the models and utils directories
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # Add ROOT to sys.path

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, colorstr, cv2,
                           increment_path, non_max_suppression, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode
from utils.augmentations import letterbox

class YOLOv9Node(Node):
    def __init__(self):
        super().__init__('yolov9_node')

        # Load parameters from the launch file
        # Load parameters from the launch file, expanding environment variables
        self.weights = os.path.expandvars(self.declare_parameter('weights', str(ROOT / 'yolov9/gelan-c.pt')).value)
        self.source = self.declare_parameter('source', 'ros').value
        self.imgsz = self.declare_parameter('imgsz', [480, 640]).value
        self.conf_thres = self.declare_parameter('conf_thres', 0.8).value
        self.iou_thres = self.declare_parameter('iou_thres', 0.45).value
        self.max_det = self.declare_parameter('max_det', 1000).value
        self.device = self.declare_parameter('device', '0').value
        self.view_img = self.declare_parameter('view_img', True).value
        self.save_txt = self.declare_parameter('save_txt', False).value
        self.save_conf = self.declare_parameter('save_conf', False).value
        self.save_crop = self.declare_parameter('save_crop', False).value
        self.nosave = self.declare_parameter('nosave', False).value
        self.classes = self.declare_parameter('classes', None).value
        self.agnostic_nms = self.declare_parameter('agnostic_nms', False).value
        self.augment = self.declare_parameter('augment', False).value
        self.visualize = self.declare_parameter('visualize', False).value
        self.update = self.declare_parameter('update', False).value
        self.project = os.path.expandvars(self.declare_parameter('project', str(ROOT / 'yolov9/runs/detect')).value)
        self.name = self.declare_parameter('name', 'exp').value
        self.exist_ok = self.declare_parameter('exist_ok', False).value
        self.line_thickness = self.declare_parameter('line_thickness', 3).value
        self.hide_labels = self.declare_parameter('hide_labels', False).value
        self.hide_conf = self.declare_parameter('hide_conf', False).value
        self.half = self.declare_parameter('half', False).value
        self.dnn = self.declare_parameter('dnn', False).value
        self.vid_stride = self.declare_parameter('vid_stride', 1).value
        self.data = os.path.expandvars(self.declare_parameter('data', str(ROOT / 'yolov9/data/coco128.yaml')).value)

        # Add new parameters for input and output topics
        self.input_topic = self.declare_parameter('input_topic', '/camera/image_raw').value
        self.output_topic_image = self.declare_parameter('output_topic_image', '/yolov9/annotated_image').value
        self.output_topic_detections = self.declare_parameter('output_topic_detections', '/yolov9/detections').value

        self.bridge = CvBridge()

        # Initialize model
        device = select_device(self.device)
        self.model = DetectMultiBackend(self.weights, device=device, data=None, fp16=False)
        self.stride, self.names, self.pt = self.model.stride, self.model.names, self.model.pt
        self.model.warmup(imgsz=(1, 3, *self.imgsz))

        # Subscription to the input image topic
        self.subscription = self.create_subscription(
            Image,
            self.input_topic,  # Use the parameter value
            self.camera_callback,
            10
        )

        # Publisher for detections
        self.detection_publisher = self.create_publisher(YoloDetection, self.output_topic_detections, 10)
        
        # Publisher for annotated image
        self.image_publisher = self.create_publisher(Image, self.output_topic_image, 10)



    @smart_inference_mode()
    def run(self, cv_image):
        dataset = self.preprocess(cv_image)
        path, im, im0s = dataset

        dt = (Profile(), Profile(), Profile())

        with dt[0]:
            im = torch.from_numpy(im).to(self.model.device)
            im = im.half() if self.model.fp16 else im.float()
            im /= 255
            if len(im.shape) == 3:
                im = im[None]

        with dt[1]:
            pred = self.model(im, augment=False)
            pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, self.classes, self.agnostic_nms, max_det=self.max_det)

        with dt[2]:
            for i, det in enumerate(pred):
                if len(det):
                    det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0s.shape).round()

                    annotator = Annotator(im0s, line_width=3, example=str(self.names))
                    for *xyxy, conf, cls in reversed(det):
                        # Calculate the center of the bounding box
                        x_center = float((xyxy[0] + xyxy[2]) / 2)
                        y_center = float((xyxy[1] + xyxy[3]) / 2)

                        # Publish detection using custom message with center coordinates
                        detection_msg = YoloDetection()
                        detection_msg.class_name = self.names[int(cls)]
                        detection_msg.confidence = conf.item()
                        detection_msg.x_min = float(xyxy[0])
                        detection_msg.y_min = float(xyxy[1])
                        detection_msg.x_max = float(xyxy[2])
                        detection_msg.y_max = float(xyxy[3])
                        detection_msg.x_center = x_center  # Set the center x-coordinate
                        detection_msg.y_center = y_center  # Set the center y-coordinate

                        self.detection_publisher.publish(detection_msg)

                        # Annotate image with bounding box and confidence
                        label = f'{self.names[int(cls)]} {conf:.2f}'
                        annotator.box_label(xyxy, label, color=colors(int(cls), True))

                    im0 = annotator.result()

                    # Publish annotated image to topic
                    annotated_msg = self.bridge.cv2_to_imgmsg(im0, encoding="bgr8")
                    self.image_publisher.publish(annotated_msg)

                    # Optionally display the image in a window
                    if self.view_img:
                        cv2.imshow("YOLOv9 Detection", im0)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            cv2.destroyAllWindows()
                            rclpy.shutdown()


    def camera_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if cv_image is not None:
            self.run(cv_image)

    def preprocess(self, im):
        im0 = im.copy()
        im = np.array([letterbox(im, self.imgsz, stride=self.stride, auto=self.pt)[0]])
        im = im[..., ::-1].transpose((0, 3, 1, 2))
        im = np.ascontiguousarray(im)
        return self.source, im, im0

def main(args=None):
    rclpy.init(args=args)

    node = YOLOv9Node()
    try:
        rclpy.spin(node)
    finally:
        cv2.destroyAllWindows()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

