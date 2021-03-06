#!/usr/bin/env python
import roslib; roslib.load_manifest('kinect_follower')
import rospy
import pygame.display
import pygame.image
#from std_msgs.msg import String
import os


def callbackscreen(message):
    if message.data == "full":
        screenplane = pygame.display.set_mode((0,0),pygame.FULLSCREEN ,0)
        displayPicture()
        #rospy.loginfo(rospy.get_name()+" Switching to fullscreen mode")
    elif message.data == "close":
        os.system("xrandr -o right")
        screenplane = pygame.display.set_mode((0,0),0,0)
        displayPicture()
        #rospy.loginfo(rospy.get_name()+" Closing fullscreen mode")

def displayPicture():
    screenplane.blit(picture, (0, 0))
    pygame.display.update()

def callback(message):
    global picture
    if state1 == 0:
        state1++
        picture = can1
    elif state1 == 1:
        state1++
        picture = can2
    elif state1 == 2:
        state1++
        picture = can3
    elif state1 == 3:
        state1++
        picture = can4
    elif state1 == 4:
        state1 = 0
        picture = can5

    displayPicture()

def screen():
    #rospy.Subscriber("screen",String, callbackscreen)
    rospy.Subscriber('movement_state',String, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('screen')
    os.system("xrandr -o normal")
    pygame.display.init()
    screenplane = pygame.display.set_mode((0,0),pygame.FULLSCREEN ,0)
    pckpath = roslib.packages.get_pkg_dir("kinect_follower")
    #bottle_pic = pygame.image.load(pckpath+"/bottle.png")
    #bottle_pic = pygame.transform.rotate(bottle_pic, -90)
    #picture = bottle_pic
    displayPicture()
    try:
        screen()
    except rospy.ROSInterruptException: pass
