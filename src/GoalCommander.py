#!/usr/bin/env python3

import rospy
import pyaudio
import time
import speech_recognition as sr

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

r = sr.Recognizer()
cafebot_state = 3


KeyWord = {"ไปห้องแรก":"Room_1",
            "ไปห้อง 1":"Room_1",
            "ไปห้อง 2":"Room_2",
            "ไปห้อง 3":"Room_3",
            "ไปห้อง 4":"Room_4",
            "ไปห้อง 5":"Room_5",
            "ไปห้อง 6":"Room_6",
            "ไปห้องสุดท้าย":"Room_6"}



Goal = {"Room_1":[-5.018,1.109,-0.6601,0.7511],
        "Room_2":[-5.565,4.032,-0.684,0.728],
        "Room_3":[-6.212,6.739,-0.646,0.7629],
        "Room_4":[-2.391,7.666 ,-0.64,0.7679],
        "Room_5":[-1.7639,4.6641,-0.670,0.742],
        "Room_6":[-1.256,2.0788,-0.66,0.751],
        "Standby_Station":[-5.69,-1.0,0.1304,0.9914]}




def movebase_client(map_odom_desire):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = map_odom_desire[0]
    goal.target_pose.pose.position.y = map_odom_desire[1]
    goal.target_pose.pose.orientation.z = map_odom_desire[2]
    goal.target_pose.pose.orientation.w = map_odom_desire[3]

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        
        while 1:
            try:
                rospy.loginfo("Setting MIC: Say Something . . .")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    word = r.recognize_google(audio,language='th')
                    rospy.loginfo("Mic testing . . . STATUS: OK")
                    break

            except:
                rospy.loginfo("Setting MIC: Say Something . . .")



        while 1:
            if (cafebot_state == 0):
               rospy.loginfo("ready to get command")
               cafebot_state = 1

            elif (cafebot_state == 1):  
                try:
                    with sr.Microphone() as source:                
                        audio = r.listen(source)
                        word = r.recognize_google(audio,language='th')
                        try:
                            rospy.loginfo("Going to . . . " + KeyWord[word])
                            result = movebase_client(Goal[KeyWord[word]])
                            if result:
                                rospy.loginfo("Arrive at desired room")
                                cafebot_state = 2
                        except:
                            rospy.loginfo("Can't decode your voice, pls say again pls")
                            rospy.loginfo("Command Example : ไปห้องแรก")
                            pass

                except:
                    pass

            elif (cafebot_state == 2):  
                rospy.loginfo("Wait for customer interaction . . .")
                time.sleep(10)
                rospy.loginfo("Back to Standby-Station")
                cafebot_state = 3
            
            elif (cafebot_state == 3):
                rospy.loginfo("Going to . . . Standby_Station")
                result = movebase_client(Goal["Standby_Station"])
                if result:
                    rospy.loginfo("Arrive at the Standby-Station")
                    rospy.loginfo("Standby for Titan-Fall !!!")
                    cafebot_state = 0
            




    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
