#!/usr/bin/env python3
import rospy
from human_robot_interaction_system.msg import RobotState
from std_msgs.msg import String

def robot_state_callback(msg):
    rospy.loginfo("Received Robot State: %s", msg)

def main():
    rospy.init_node('robot_interaction_node')

    # Subscribe to a topic (like 'human_gesture')
    rospy.Subscriber('human_gesture', String, robot_state_callback)

    # Publish robot state on a topic
    pub = rospy.Publisher('robot_state', RobotState, queue_size=10)

    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        robot_state = RobotState()
        robot_state.robot_name = "HR-Robot"
        robot_state.current_task = "Waiting for Gesture"
        robot_state.is_interacting = False

        pub.publish(robot_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
