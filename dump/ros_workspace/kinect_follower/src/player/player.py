#!/usr/bin/env python

# Remember the two lines for every python ROS node? 
import roslib
roslib.load_manifest('kinect_follower')

# Load (import) rospy
import rospy
import pygame
from geometry_msgs.msg import Twist

class SoundPlayer:

    def __init__(self):
	rospy.Subscriber("cmd_vel", Twist, self.playerCallback)

    def playerCallback(self, data):
	if data.linear.x != 0 and state1 == False:
	    pygame.mixer.Sound('/home/human/ros_workspace/kinect_follower/Hi.wav').play()
	    state1 = True
	    
	if data.linear.x == 0 and state1 == True:
	    pygame.mixer.Sound('/home/human/ros_workspace/kinect_follower/Cans.wav').play()
	    state1 = False

    def startListener(self):
	rospy.spin()

if __name__ == '__main__':
    try:
        # instantiate the class and start the listener
	    rospy.init_node("player")
	    pygame.init()
        jsconv = SoundPlayer()
        jsconv.startListener()
    except rospy.ROSInterruptException: 
        pass
	
