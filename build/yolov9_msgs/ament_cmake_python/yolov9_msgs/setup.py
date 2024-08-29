from setuptools import find_packages
from setuptools import setup

setup(
    name='yolov9_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('yolov9_msgs', 'yolov9_msgs.*')),
)
