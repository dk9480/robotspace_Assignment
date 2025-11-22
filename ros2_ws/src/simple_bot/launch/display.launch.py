from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    urdf_path = '/home/kalaiyarasan/ros2_ws/src/simple_bot/urdf/simple_bot.urdf'

    return LaunchDescription([
        Node(
            package='simple_bot',
            executable='marker_tf',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': open(urdf_path).read()
            }],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        ),
    ])
