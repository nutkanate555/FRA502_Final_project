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
