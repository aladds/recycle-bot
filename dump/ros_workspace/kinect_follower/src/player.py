#!/usr/bin/env python

# Remember the two lines for every python ROS node? 
import roslib
roslib.load_manifest('ros_intro')

# Load (import) rospy
import rospy
import pygame
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Speaker:

    def __init__(self):
	rospy.Subscriber('cmd_vel', Twist, self.playerCallback)
	pub = rospy.Publisher('movement_state', String)

    def playerCallback(self, data):
	if data.linear.x != 0 and state1 == False:
	    pygame.mixer.Sound('/home/human/recycle-bot/dump/ros-workspace/kinect_follower/hithere.wav').play()
	    state1 = True
	    
	if data.linear.x == 0 and state1 == True:
	    pygame.mixer.Sound('/home/human/recycle-bot/dump/ros-workspace/kinect_follower/gotacan.wav').play()
	    state1 = False
	    pub.publish('next')

    def startListener(self):
	rospy.spin()

if __name__ == '__main__':
    try:
        # instantiate the class and start the listener
	rospy.init_node("player")
	    pygame.init()
        jsconv = Speaker()
        jsconv.startListener()
    except rospy.ROSInterruptException: 
        pass
	
