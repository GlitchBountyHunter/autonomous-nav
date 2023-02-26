#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 0.25
    goal.target_pose.pose.position.y = 0.0    
    goal.target_pose.pose.position.z = 0

    goal.target_pose.pose.orientation.w = -0.3
    goal.target_pose.pose.orientation.z = 0.95


    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("[ ERROR ] Action server  ;/ ")

if __name__ == '__main__':
    try:
        rospy.init_node('movebaseClient')
        result = movebase_client()
        if result:
            rospy.loginfo("i reached the goal ")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation DONE ")
