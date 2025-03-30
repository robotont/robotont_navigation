from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    gamepad_conf_decl = DeclareLaunchArgument('gamepad_conf', default_value='dualsense.yaml')

    config = os.path.join(
        get_package_share_directory('robotont_navigation'),
        'config',
        'joy',
        LaunchConfiguration('gamepad_conf')
    )

    return LaunchDescription([
        gamepad_conf_decl,
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen'
        ),
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy',
            parameters=[config],
            output='screen'
        )
    ])
