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
        rospy.loginfo(rospy.get_name()+" Switching to fullscreen mode")
    elif message.data == "close":
        os.system("xrandr -o right")
        screenplane = pygame.display.set_mode((0,0),0,0)
        displayPicture()
        rospy.loginfo(rospy.get_name()+" Closing fullscreen mode")

def displayPicture():
    screenplane.blit(picture, (0, 0))
    pygame.display.update()


def callback(message):
    global picture
    if message.bottle == 0:
        picture = bottle_cross
        rospy.loginfo(rospy.get_name()+" Detected not bottle")
    elif message.bottle == 1:
        picture = bottle_tick
        rospy.loginfo(rospy.get_name()+" Bottle detected")
    else:
        picture = bottle_pic

    displayPicture()

def screen():
    rospy.init_node('screen')
    #rospy.Subscriber("screen",String, callbackscreen)
    rospy.spin()

if __name__ == '__main__':
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
