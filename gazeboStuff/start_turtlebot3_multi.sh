#! /usr/bin/env bash

# We remove a folder that otherwise gives issues in ROS2 launches
sudo rm -rf /home/user/.ros

# We set up the environment for ROS2
. /usr/share/gazebo/setup.sh
. /install/setup.bash

ros2 launch turtlebot3_gazebo turtlebot3_tc_world_two_robots.launch.py
