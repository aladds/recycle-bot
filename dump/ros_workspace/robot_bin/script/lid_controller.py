#!/usr/bin/env python

import roslib
roslib.load_manifest('robot_bin')

import rospy
from geometry_msgs.msg import Twist
import serial
state1 = False

class LidController:
	def __init__(self):
		rospy.init_node("lid_controller")
		rospy.Subscriber("cmd_vel", Twist, self.playerCallback)
		ser = serial.serial_for_url('/dev/ttyUSB1') # open first serial/USB port, change as needed
		print ser.portstr       # check which port was really used

	def playerCallback(self, data):
		global state1
		
		if data.linear.x < 0.1 and state1 == False:
			ser.write("SM0.\n") #open the lid
			state1 = True
			
		if data.linear.x > 0.2 and state1 == True:
			ser.write("SM100.\n") #close the lid 
			state1 = False

	def startListener(self):
		rospy.spin()

if __name__ == '__main__':
	try:
		sp = LidController()
		sp.startListener()
	except rospy.ROSInterruptException:
		pass
	
