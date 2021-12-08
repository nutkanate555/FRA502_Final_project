# FRA502_Final_project
## Introduction
 This project is a part of "Service Robot" Subject.

## Build and Develop By
 MR.Nutkanate Apikomchatkup\
 Nickname: Tin\
 ID: 62340500017\
 Year 3 Semester 1\
 FIBO KMUTT FRAB6
 
## Contact
 FB: Nutkanate Apikomchatkup
 
## Task of  this robot:
 This robot is made for delivery the snack or somethings else in the karaoke bars.
 
## Requirement
 1. ros plugin: amcl, gmapping, map_server, rospy, movebase, actionlib
 2. python library: SpeechRecognition, Pyaudio
 
## Context:
 1. URDF Creation and World creation in gazebo.
 2. Using Laser scan topic (hokuyo) : Gmapping and Localization with amcl.
 3. ROS Navigation with movebase [Rolling local planner].
 4. Goal Pubisher for Movebase plugin.
 5. System of this robot: inform of StateMachine. Command by using SpeechRecognition in Thai language.

## Installation:
1. Install Robotics Operating System (ROS) : In this project,I using ROS noetic.\
   Follow these instruction to install ROS.\
   Link: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
2. Clone this project and drop it in your "/src" folder in your "catkin_ws/src" ,\ 
   If these files are in zip format don't forget to extact them.
3. Open terminal and run 
```
catkin_make
```
4. Finish, Have Fun.

## How to run this project step by step
1. Go to your catkin_ws by using
```
cd ~/catkin_ws
source devel/setup.bash
```
2. Launch the project via terminal by using
```
roslaunch FRA502_Final_project all_in_one.launch
```
3. Let's test my project!!!. XD

## How to command this robot
1. Firstly robot will let's user say something to test microphone and go to "Standby station"
2. After the robot arrive at "Standby station" user will have 6 choice to command the robot to let it go to user's desire room.\
   This is the command:
```
"ไปห้อง x" => Go to room x
```
 Note 0: My woold have 6 rooms so "x" will be "1-6"\
 Note 1: My robot's commands are in Thai language, So, when user command the nummber such as, "1" : the user should spell "หนึ่ง" to command my robot.
 3. My robot will go to the desire room and back to Standby station. and wait for new command. [look command at 2.]
 
 ## The problems that I ever found while doing this project.
 1. "joint state pubisher" and "gazebo" sending the TF to RVIZ at the same time. So, it cause glitching visualization in RVIZ.\ 
    And I fix this problem by remove the "joint state pubisher" from my rviz file.\
 2. the odometry of the robot in "map" and "gazebo" aren't the same when I rotate my robot.\
    The solution to fix this problem is:\
    2.1. Add some mass to my robot.\
    2.2. Tuning the "wheel_separation multiplier" in "config.yaml" file.\
 3. Can't install pyaudio on my env.\
    The solution to fix this problem is:\
```
sudo apt-get install python3-pip
sudo apt-get install portaudio19-dev
sudo apt-get install python-pyaudio
pip install PyAudio
```
