import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    yolov9_config_path = os.path.join(
        get_package_share_directory('yolov9'),
        'config',
        'yolov9.yaml'
    )

    return LaunchDescription([
        Node(
            package='yolov9',
            executable='detector',
            name='detector',
            parameters=[yolov9_config_path],
            output='screen'
        ),
    ])

