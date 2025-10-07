import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class SimpleParam(Node):
    def __init__(self):
        super().__init__("simple_param")
        self.declare_parameter("simple_init_param", 28)
        self.declare_parameter("simple_string_param", "Julius")

        self.add_on_set_parameters_callback(self.paramChangeCallback)

    def paramChangeCallback(self, params):
        result = SetParametersResult()

        for param in params:
            if param.name == "simple_int_param" and param.type == Parameter.Type.INTEGER:
                set.get_logger().info("Param simple_int_param changed! New value is: %d" %param.value)
                result.successful = True

            if param.name == "simple_string_param" and param.type == Parameter.Type.STRING:
                set.get_logger().info("Param simple_string_param changed! New value is: %d" %param.value)
                result.successful = True

        return result
    
def main():
    rclpy.init()
    simple_param = SimpleParam()
    rclpy.spin(simple_param)
    simple_param.destroy_node()
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()