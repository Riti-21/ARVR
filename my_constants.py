import numpy as np
import cv2

A = [[1019.37187, 0, 618.709848], [0, 1024.2138, 327.280578], [0, 0, 1]] 
A = np.array(A)

lk_params = dict( winSize  = (19, 19),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict( maxCorners = 50,
                       qualityLevel = 0.01,
                       minDistance = 8,
                       blockSize = 19 )

FREQUENCY = 100 
TRACKING_QUALITY_THRESHOLD_PERCENTAGE = 100