import rclpy
from rclpy.node import Node
from my_interfaces.msg import Bool

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("starter") 
        self.cmd_vel_pub = self.create_publisher(Bool, "start", 1 ) 
        
        timer_period = 1/30 #seconds
        self.timer = self.create_timer(timer_period,self.send_velocity_command) 
        self.get_logger().info("the process has been started")

    
    def send_velocity_command(self):
        msg = Bool() 
        msg.data = True
        self.cmd_vel_pub.publish(msg) 


def main(args=None):
    rclpy.init(args=args) 
    node = DrawCircleNode() 
    rclpy.spin(node)
    rclpy.shutdown() 

if __name__ == '__main__':
    main()

    
#colcon build --symlink-install --packages-select cv_basics
