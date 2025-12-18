#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Yusaku Aka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class DZoneFilterNode(Node):
    def __init__(self):
        super().__init__('filter_node')
        
        # パラメータ
        self.declare_parameter('zone', 0.1)
        self.last_sent_value = 0.0
        
        # サブスクライバ
        self.subscription = self.create_subscription(
            Float64, 'input_value', self.listener_callback, 10)
        
        # パブリッシャ
        self.publisher = self.create_publisher(Float64, 'output_value', 10)

    def listener_callback(self, msg):
        zone = self.get_parameter('zone').get_parameter_value().double_value
        
        current_input = msg.data
        diff = abs(current_input - self.last_sent_value)

        if diff > zone:
            self.last_sent_value = current_input
            
        # 出力用メッセージの作成送信
        output_msg = Float64()
        output_msg.data = self.last_sent_value
        self.publisher.publish(output_msg)
        self.get_logger().info(f'{output_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = DZoneFilterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
