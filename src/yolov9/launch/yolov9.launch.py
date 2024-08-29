#!/usr/bin/env python3
# YOLOv9 ROS2 Launch File
# Created by: Xavier Vicent
# Email: xvicentnavar2024@fau.edu
# Description: This launch file starts the YOLOv9 object detection node in ROS2.
#              If you use or reference this code, please give appropriate credit.
import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='yolov9',  # Replace with your actual package name
            executable='detector',  # Replace with the actual executable name
            name='detector',
            output='screen',
            parameters=[os.path.expanduser('~/yolov9_ros/src/yolov9/config/yolov9.yaml')]
  # Replace with the path to your YAML file
        ),
    ])

