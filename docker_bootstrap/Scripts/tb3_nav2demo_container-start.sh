#!/usr/bin/env bash


gnome-terminal -- bash -c "ros2 launch turtlebot3_gazebo turtlebot3_tc_world_two_robots.launch.py exec bash"
#gnome-terminal -- bash -c "source /opt/ros/galactic/setup.bash; exec bash"
#gnome-terminal -- bash -c "apt-get update && apt-get upgrade -y; rosdep update; rosdep install --from-path src --ignore-src -y; exec bash"
bash # Prevents container from closing
