#! /usr/bin/python
#system level imports
import sys, os
import numpy as np
import scipy.io as sio
import time

#needed modules and classes that are specific to baxter control
from math import pi
from baxter_interface.limb import Limb
from rad_baxter_limb import RadBaxterLimb
from baxter_pykdl import baxter_kinematics as b_kin
import rospy
import tf


if __name__ == '__main__':
    
    # this code is specific to the way we are communicating over the
    # network, you could name it anythin you want
    rospy.init_node('me_537_project')

    # here we instantiate a baxter limb object that can allow us to
    # get data and set commanded joint angles
    limb = RadBaxterLimb('left')

    # this sets the maximum allowable speed, can go up to 1 or down to 0, be careful please
    limb.set_joint_position_speed(0.2)

    # this defines how long we wait to send a new command in Hz 
    control_rate = rospy.Rate(.1)
    
    # baxter will time-out for safety reasons if we don't continually
    # send a command, so this loop allows us to send commands at the
    # specified rate
    while not rospy.is_shutdown():

        # you would need to put your code here to change the joint
        # angle command which for this example is set to zero
        limb.set_joint_positions_mod([0 -pi/6 0 4*pi/6 pi/2 0 0])
  
        # causes the loop to sleep for 10 of a second (approximately)
        control_rate.sleep()

        # you would need to put your code here to change the joint
        # angle command which for this example is set to zero
        #limb.set_joint_positions_mod([0 -pi/6 0 4*pi/6 pi/2 pi/3 0])
  
        # causes the loop to sleep for 10 of a second (approximately)
        #control_rate.sleep()

                # you would need to put your code here to change the joint
        # angle command which for this example is set to zero
        #limb.set_joint_positions_mod([0 -pi/6 0 4*pi/6 pi/2 -pi/3 0])
  
        # causes the loop to sleep for 10 of a second (approximately)
        #control_rate.sleep()

                # you would need to put your code here to change the joint
        # angle command which for this example is set to zero
        #limb.set_joint_positions_mod([0 -pi/6 0 4*pi/6 pi/2 0 0])
  
        # causes the loop to sleep for 10 of a second (approximately)
        #control_rate.sleep()
        #control_rate.sleep()
        #control_rate.sleep()            

