from setuptools import setup
from glob import glob

package_name = 'yolov9'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=[
        'rclpy',
        'opencv-python',  # If you are using OpenCV
        'torch',          # If you are using PyTorch
        'numpy',          # If you need NumPy
    ],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='YOLOv9 object detection package for ROS 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detector = yolov9.detect_ros:main',  # Replace with the actual entry point
            'stream = yolov9.stream:main',  # Replace with the actual entry point
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name,
            glob('launch/*.py')),  # Include all Python launch files in the 'launch' directory
    ],
    setup_requires=['setuptools'],
)
