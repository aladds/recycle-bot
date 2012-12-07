#!/usr/bin/env python

import roslib
roslib.load_manifest('robot_bin')

import rospy
import pygame
from geometry_msgs.msg import Twist
state1 = False

class SoundPlayer:
	def __init__(self):
		rospy.init_node("player")
		rospy.Subscriber("cmd_vel", Twist, self.playerCallback)
		pygame.init()

	def playerCallback(self, data):
		global state1
		
		if data.linear.x < 0.1 and state1 == False:
			pygame.mixer.Sound('/home/human/ros_workspace/robot_clips/Hi.wav').play()
			state1 = True
			
		if data.linear.x > 0.2 and state1 == True:
			pygame.mixer.Sound('/home/human/ros_workspace/robot_clips/HeyYou.wav').play()
			state1 = False

	def startListener(self):
		rospy.spin()

if __name__ == '__main__':
	try:
		sp = SoundPlayer()
		sp.startListener()
	except rospy.ROSInterruptException:
		pass
	
