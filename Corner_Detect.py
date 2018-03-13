import cv2
import numpy as np

img = cv2.imread("spideropencv.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#Best corner detection method than cv2.cornerHarris
#Generally used for tracking

corners = cv2.goodFeaturesToTrack(gray,20,.1,100)
corners = np.int0(corners)

for corner in corners:
	x,y = corner.ravel()
	cv2.circle(img ,(x,y) ,3 ,255 ,-1)

cv2.imshow("COrners",img)

cv2.waitKey(100000)
