#!/bin/bash

sudo apt-get update
sudo apt-get install ros-kinetic-ros-numpy
sudo apt-get install ros-kinetic-joint-trajectory-controller
sudo apt-get install ros-kinetic-serial
sudo apt-get install ros-kinetic-effort-controllers 
sudo apt-get install ros-kinetic-dynamixel-controllers 


chmod +x run_gazebo.sh
chmod +x run_navigation.sh
chmod +x run_go_to_table.sh