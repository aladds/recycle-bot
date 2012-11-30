/*
 * Copyright (c) 2012 Miguel Sarabia del Castillo
 * Imperial College London
 *
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 */

#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/Twist.h>
#include <time.h>
#include <stdlib.h>


// README: The objective of this part is to obtain the position of the user's
// torso with respect to the base of the robot, and then create a velocity
// command so robot follows the user.

std::string getOriginFrame()
{
        static int torso_num = 0;
        std::string chosen_torso;
        std::string torso_list[] = {    "torso_1",
                                        "torso_2",
                                        "torso_3",
                                        "torso_4",
                                        "torso_5" };
        
        
        srand(time(NULL));
        torso_num++;
        if(torso_num>4)torso_num=0;
        
        
        chosen_torso = torso_list[torso_num];
        
        
        
        std::cout << chosen_torso << std::endl;
        
        return chosen_torso;
}

int main(int argc, char* argv[])
{
    // WARNING: Safety-critical constants, please do not modify.
    const double frequency = 20;
    const double timeToUser = 6; //Time for robot to reach to user's position
    const double minDistance = 0.2; //30 cm
    const double minAngle = 0.09; //~5deg
    const double maxLinearSpeed = 0.3;// in metres per second
    const double maxAngularSpeed = 0.52; //~30 deg per second

    // Initialise ROS
    ros::init(argc, argv, "kinect_follower");
    ros::NodeHandle nodeHandle;
    ros::Rate nodeRate(frequency); //Node runs at 20Hz

    //Advertise cmd_vel
    ros::Publisher pub = nodeHandle.advertise<geometry_msgs::Twist>(
                "cmd_vel", 10
                );

    // Maximum time for transform to be available
    const double timeout = 0.1;
    //const std::string originFrame = "torso_1";
    const std::string destFrame = "base_link";


    tf::TransformListener tfl;

    while( ros::ok() )
    {
        double linearSpeed = 0.0;
        double angularSpeed = 0.0;
        std::string originFrame = getOriginFrame();

        bool okay = tfl.waitForTransform(
                    destFrame,
                    originFrame,
                    ros::Time::now() - ros::Duration(timeout), //Need recent tf
                    ros::Duration(timeout)
                    );

        if ( okay )
        {
            
            geometry_msgs::PointStamped input;
            input.header.frame_id = originFrame;
            input.header.stamp = ros::Time(0);

            input.point.x = 0.0;
            input.point.y = 0.0;
            input.point.z = 0.0;

            geometry_msgs::PointStamped output;

            tfl.transformPoint( destFrame, input, output );


            double distance = std::sqrt(
                        output.point.x * output.point.x +
                        output.point.y * output.point.y
                        );

            double angle = std::atan2(output.point.y, output.point.x);


            if ( std::abs(angle) > minAngle )
            {
                angularSpeed = std::abs( angle*frequency / timeToUser );

                if (angularSpeed > maxAngularSpeed)
                    angularSpeed = maxAngularSpeed;


                if ( angle < 0 )
                    angularSpeed = -angularSpeed;

            }
            if ( distance > minDistance )
            {
                linearSpeed =  distance * frequency /timeToUser ;

                if (linearSpeed > maxLinearSpeed)
                    linearSpeed = maxLinearSpeed;

            }
        }

        geometry_msgs::Twist msg;

        msg.linear.x = linearSpeed;
        msg.angular.z = angularSpeed;

        std::cout << "Angular speed is " << angularSpeed << "," << "Linear speed is " << linearSpeed << "." << std::endl;

        pub.publish(msg);

        ros::spinOnce();
        nodeRate.sleep();
    }

    return 0;
}
