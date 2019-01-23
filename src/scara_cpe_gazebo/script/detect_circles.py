#!/usr/bin/env python
from __future__ import print_function

import roslib
import ros_numpy

import sys
import rospy

import cv2
import numpy as np
import message_filters
from std_msgs.msg import String
from sensor_msgs.msg import Image
from sensor_msgs.point_cloud2 import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from cv_bridge import CvBridge, CvBridgeError

class ImageHandler:

	def __init__(self, only_one_call):

		self.bridge = CvBridge()

		self.circles_coordinates_in_image = []
		self.circles_coordinates_in_world = []

		self.coordinates_camera = [1.656235, -0.801825, 1.147801]

		#coordinates_model = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)  # [1.656235, -0.801825, 1.147801]
    	#coordinates_camera = coordinates_model('camera', 'world').pose.position

    	#self.coordinates_camera = [coordinates_camera.x, coordinates_camera.y, coordinates_camera.z]
    	


	def compute_coordinates(self):
		image_sub = rospy.wait_for_message("/camera_top/image_raw", Image)
		point_cloud_sub = rospy.wait_for_message("camera_top/depth/points", PointCloud2)

		self.image_conversion_to_openCV_image(image_sub)
		
		self.circle_detection()

		self.get_coordinates(point_cloud_sub)


	def image_conversion_to_openCV_image(self, data):
	    try:
	        self.image = self.bridge.imgmsg_to_cv2(data, "bgr8")

	    except CvBridgeError as e:
	        print(e)

	def circle_detection(self):
	  	try:

			img = self.image
	        
			img = cv2.medianBlur(img, 3)

			cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

			circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,
	                            	   param1=50,param2=30,minRadius=0,maxRadius=0)

			circles = np.uint16(np.around(circles))

			number_of_circles_found = 0

			for i in circles[0,:]:

				# draw the outer circle
				cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
				# draw the center of the circle
				cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

				self.circles_coordinates_in_image.append([i[0], i[1]])

				number_of_circles_found += 1

			rospy.loginfo(" ## Detection step : " + str(number_of_circles_found) + " circles found")

	  	except:
	  		print("Error in circle detection")

	def get_coordinates(self, data):
	    try:
	        cloud_points = []

	        point_cloud = pc2.read_points(data, skip_nans=True, field_names=("x", "y", "z"))  # Get the coordinates of each pixel on the picture, x, y are the only important 1, z is the same = camera z
	        point_cloud_coordinates_array = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(data)
	        
	        for circle_position in self.circles_coordinates_in_image:
	            pixel_x = circle_position[0]
	            pixel_y = circle_position[1]

	            pcl_index = pixel_x*data.width + pixel_y  # The list of pixel is one dimensional, with height*width elements

	            coin_pos = self.coordinates_camera - point_cloud_coordinates_array[pcl_index] 
	            self.circles_coordinates_in_world.append(coin_pos)

	        rospy.loginfo(" ## Coordinates computation step : coordinates found")

	    except Exception, e:
	        print(e)

def detect_circles(only_one_call = True):
	ic = ImageHandler(only_one_call)

  	#rospy.init_node('circle_detection', anonymous=True)

  	try:
		ic.compute_coordinates()
  	except:
		print("Shutting down")

	print("Hello")
  	
  	return ic.circles_coordinates_in_world