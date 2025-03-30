from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_dir = get_package_share_directory('robotont_navigation')
    default_params = os.path.join(pkg_dir, 'config', 'nav', 'nav2_realsense.yaml')
    depth_to_scan_params = os.path.join(pkg_dir, 'config', 'nodes', 'depth_image_to_laserscan.yaml')
    slam_params = os.path.join(pkg_dir, 'config', 'nodes', 'slam.yaml')

    use_sim_time_decl = DeclareLaunchArgument('use_sim_time', default_value='true')
    params_decl = DeclareLaunchArgument('params_file', default_value=default_params)
    image_decl = DeclareLaunchArgument('image', default_value='/camera/depth/image_raw')
    info_decl = DeclareLaunchArgument('info', default_value='/camera/color/camera_info')
    scan_decl = DeclareLaunchArgument('scan', default_value='/scan')

    depth_to_laser = Node(
        package='depthimage_to_laserscan',
        executable='depthimage_to_laserscan_node',
        name='depthimage_to_laserscan',
        parameters=[depth_to_scan_params, {'use_sim_time': LaunchConfiguration('use_sim_time')}],
        remappings=[
            ('depth', LaunchConfiguration('image')),
            ('depth_camera_info', LaunchConfiguration('info')),
            ('scan', LaunchConfiguration('scan'))
        ],
        output='screen'
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_dir, 'launch', 'nav2_bringup.launch.py')
        ),
        launch_arguments={
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'params_file': LaunchConfiguration('params_file')
        }.items()
    )

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('slam_toolbox'), 'launch', 'online_sync_launch.py')
        ),
        launch_arguments={
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'params_file': slam_params
        }.items()
    )

    return LaunchDescription([
        use_sim_time_decl,
        params_decl,
        image_decl,
        info_decl,
        scan_decl,
        depth_to_laser,
        nav2,
        slam
    ])
