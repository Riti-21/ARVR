import cv2
import numpy as np
from object_module import *
import aruco_module as aruco 
from my_constants import *
from utils import get_extended_RT
from tkinter import*

class animal:
	def __init__(self,root):
		obj = three_d_object('data/3d_objects/low-poly-fox-by-pixelmannen.obj', 'data/3d_objects/texture.png')
		marker_colored = cv2.imread('data/m1.png')
		assert marker_colored is not None, "Could not find the aruco marker image file"
		marker_colored = cv2.flip(marker_colored, 1)

		marker_colored =  cv2.resize(marker_colored, (480,480), interpolation = cv2.INTER_CUBIC )
		marker = cv2.cvtColor(marker_colored, cv2.COLOR_BGR2GRAY)

		print("trying to access the webcam")
		cv2.namedWindow("webcam")
		vc = cv2.VideoCapture(0)
		assert vc.isOpened(), "couldn't access the webcam"
		
		h,w = marker.shape
		marker_sig1 = aruco.get_bit_sig(marker, np.array([[0,0],[0,w], [h,w], [h,0]]).reshape(4,1,2))
		marker_sig2 = aruco.get_bit_sig(marker, np.array([[0,w], [h,w], [h,0], [0,0]]).reshape(4,1,2))
		marker_sig3 = aruco.get_bit_sig(marker, np.array([[h,w],[h,0], [0,0], [0,w]]).reshape(4,1,2))
		marker_sig4 = aruco.get_bit_sig(marker, np.array([[h,0],[0,0], [0,w], [h,w]]).reshape(4,1,2))

		sigs = [marker_sig1, marker_sig2, marker_sig3, marker_sig4]

		rval, frame = vc.read()
		assert rval, "couldn't access the webcam"
		h2, w2,  _ = frame.shape

		h_canvas = max(h, h2)
		w_canvas = w + w2

		while rval:
			rval, frame = vc.read()
			key = cv2.waitKey(20) 
			if key == 27:
				break

			canvas = np.zeros((h_canvas, w_canvas, 3), np.uint8)
			canvas[:h, :w, :] = marker_colored

			success, H = aruco.find_homography_aruco(frame, marker, sigs)
			if not success:
				canvas[:h2 , w: , :] = np.flip(frame, axis = 1)
				cv2.imshow("webcam", canvas )
				continue

			R_T = get_extended_RT(A, H)
			transformation = A.dot(R_T) 
			
			augmented = np.flip(augment(frame, obj, transformation, marker), axis = 1)
			canvas[:h2 , w: , :] = augmented
			cv2.imshow("webcam", canvas)

		vc.release()
		cv2.destroyAllWindows()