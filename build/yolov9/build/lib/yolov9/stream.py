import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')

        # Create a CvBridge object to convert between ROS Image messages and OpenCV images
        self.bridge = CvBridge()

        # Subscribe to the image topic (change 'your_image_topic' to your actual topic name)
        self.subscription = self.create_subscription(
            Image,
            '/vision/cam/raw',
            self.image_callback,
            10)
        self.subscription  # prevent unused variable warning

    def image_callback(self, msg):
        # Convert the ROS Image message to a format OpenCV can use
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # Display the image stream
        cv2.imshow('Image Stream', cv_image)
        cv2.waitKey(3)  # Refresh the image display

def main(args=None):
    rclpy.init(args=args)

    # Create an instance of the ImageSubscriber class
    image_subscriber = ImageSubscriber()

    # Keep the node running
    rclpy.spin(image_subscriber)

    # Clean up OpenCV windows and shutdown ROS 2 when the node is stopped
    cv2.destroyAllWindows()
    image_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
