#!/usr/bin/env python  
import roslib
roslib.load_manifest('ROSIntro')
import rospy

import tf


if __name__ == '__main__':
    rospy.init_node('kinect_tf_broadcaster')
    r = rospy.Rate(50)
    try:
        br = tf.TransformBroadcaster()
        while not rospy.is_shutdown():
            br.sendTransform((0.3, 0.0, 0.15),
                             tf.transformations.quaternion_from_euler(0, 0, 0),
                             rospy.Time.now(),
                             "/camera_link",
                             "/base_link")
            r.sleep()
    except rospy.ROSInterruptException:
        pass
 
