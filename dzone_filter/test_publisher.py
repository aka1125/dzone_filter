import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class TestPublisher(Node):
    def __init__(self):
        super().__init__('test_publisher')
        self.publisher_ = self.create_publisher(Float64, 'input_value', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.val = 0.0

    def timer_callback(self):
        msg = Float64()
        msg.data = self.val
        self.publisher_.publish(msg)
        #self.get_logger().info(f'Sending: {msg.data}')
        self.val += 0.05

def main(args=None):
    rclpy.init(args=args)
    node = TestPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
