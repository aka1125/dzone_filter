from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # フィルタ
        Node(
            package='dzone_filter',
            executable='filter_node',
            name='filter',
            parameters=[{'zone': 0.1}],
            output='screen'
        ),

        # テスト送信
        Node(
            package='dzone_filter',
            executable='test_publisher',
            name='test_pub',
            output='log'
        )
    ])
