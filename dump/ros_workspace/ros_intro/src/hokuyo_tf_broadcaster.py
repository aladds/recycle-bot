#!/usr/bin/env python  
import roslib
roslib.load_manifest('ros_intro')
import rospy

import tf

if __name__ == '__main__':
    rospy.init_node('hokuyo_tf_broadcaster')
    r = rospy.Rate(50)
    rospy.loginfo("Starting Hokuyo TF Broadcaster")
    try:
        br = tf.TransformBroadcaster()
        while not rospy.is_shutdown():
            br.sendTransform((0.18, 0.0, 0.34),
                             tf.transformations.quaternion_from_euler(0, 0, 0),
                             rospy.Time.now(),
                             "laser",
                             "base_link")
                             
            r.sleep()
    except rospy.ROSInterruptException:
        pass
 
