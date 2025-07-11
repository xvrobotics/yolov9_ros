from setuptools import setup, find_packages
from glob import glob
import os

package_name = 'yolov9'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(include=[package_name, f'{package_name}.*']),
    install_requires=[
        'rclpy',
        'opencv-python',
        'torch',
        'numpy',
    ],
    zip_safe=True,
    maintainer='Xavier Vicent',
    maintainer_email='xvicentnavar2024@fau.edu',
    description='YOLOv9 object detection package for ROS 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detector = yolov9.detect_ros:main',
            'detector_2 = yolov9.detect_ros_2:main',
            'detector_3 = yolov9.detect_ros_3:main',
            'stream = yolov9.stream:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    setup_requires=['setuptools'],
)

