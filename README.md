# Coin picker project

Projects for 3 students in Barcelona which consists in the combination of a turtlebot and a robotic arm scara designed for CPE students. This mobile robot will have to pick up coins on a table, previously detected with a camera over the table, and transport them to another table.

### Prerequisites

First, clone this project in you catkin workspace and do catkin_make.
Some packages are needed to run this project. Please run the following bash file, prevent at the project root.

```
install_dependencies.sh
```

## Running the project

To run this project solution, three files need to be run in different terminals in the following order

```
run_gazebo.sh
run_navigation.sh
run_go_to_table.sh
```

Please remember that in every terminal you need to run the following command at the root of your catkin package
```
source devel/setup.bash
```

## Tools used

* Ros kinetic
* Gazebo

## Dependencies

* Scara_cpe_gazebo: rospy, std_msg
* Scara_cpe_description: control_msgs, dynamixel_controllers, dynamixel_msgs, rospy,serial, std_msgs, trajectory_msgs

## Authors

* **Abdelaziz Miyara** 
* **Marceau Fillon**
* **Sacha Piperno**  


