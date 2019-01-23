#!/bin/bash



rosrun scara_cpe_gazebo go_to_table1.py
rosrun scara_cpe_gazebo ik_service_actionclient_pos1.py
rosrun scara_cpe_gazebo go_to_table2.py
rosrun scara_cpe_gazebo ik_service_actionclient_pos2.py


