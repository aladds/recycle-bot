#!/usr/bin/env python

#the following three lines should be familiar by now. 
import roslib
roslib.load_manifest('ros_intro')

# Load (import) rospy
import rospy

# Load JoyAxis from ros_intro
from ros_intro.msg import JoyAxis

# Load Twist from geometry_msgs
from geometry_msgs.msg import Twist

# Our Joystick to Command Velocity Class
class JoystickToCmdVelConverter:

    # the CLASS initialization code
    def __init__(self, x_scale = 0.7, y_scale = 0.7):
    
        # scale the data if needed
        self.x_scale = x_scale
        self.y_scale = y_scale
        
        # initialize the node with the name 'joystick_to_cmd_vel'
        rospy.init_node('joystick_to_cmd_vel')
        
        # set up a publisher to topic 'cmd_vel' publishing Twist messages
        self.pub = rospy.Publisher('cmd_vel', Twist)
        
        # The following line creates a subcriber to the joystick topic
        # it has 3 arguments:
        #  1. the topic to subscribe to
        #  2. the message type
        #  3. the "callback" function to run when a message is received
        rospy.Subscriber("joystick", JoyAxis, self.joyCallback)
        
    # this is the callback function 
    # it is run whenever a new JoyAxis message is received
    # the received message is placed in data    
    def joyCallback(self, data):
    
        # we create a new Twist object
        cmd = Twist()
        
        # we set the variable values accordingly
        # have a look at:
        # http://www.ros.org/doc/api/geometry_msgs/html/msg/Twist.html
        # for more information about the Twist message type
        cmd.linear.x = data.x
        cmd.angular.z = data.y
        
        # Publish the new cmd message using publish
        self.pub.publish(cmd)
        
        # log the publish
        rospy.loginfo("I just published: " + str(cmd.linear.x) + ", " +
            str(cmd.linear.y))
        
    # call this function to start the listener 
    def startListener(self):
        # the rospy.spin() member function starts the callbacks
        rospy.spin()
        

# our main function
if __name__ == '__main__':
    try:
        # instantiate the class and start the listener
        jsconv = JoystickToCmdVelConverter()
        jsconv.startListener()
    except rospy.ROSInterruptException: 
        pass
        
        
