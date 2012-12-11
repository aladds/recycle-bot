#!/usr/bin/env python

import roslib
roslib.load_manifest('robot_bin')

import rospy
from std_msgs.msg import String
import serial
state1 = False

class HeadController:
	def __init__(self):
		rospy.init_node("head_controller")
		rospy.Subscriber("no_frames", String, self.playerCallback)
		ser = serial.serial_for_url('/dev/ttyUSB2') # open first serial/USB port, change as needed
		print ser.portstr       # check which port was really used

	def playerCallback(self, data):
		global state1
		
		if data.data == "true":
			if state1 == False:
				ser.write("SN0.\n") #turn left
				state1 = True
			
			if state1 == True:
				ser.write("SN100.\n") #turn right
				state1 = False
			
			rospy.sleep(3.)
		
		else
			ser.write("SN50.")

	def startListener(self):
		rospy.spin()

if __name__ == '__main__':
	try:
		sp = HeadController()
		sp.startListener()
	except rospy.ROSInterruptException:
		pass
	
