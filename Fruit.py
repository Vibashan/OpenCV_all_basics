
import numpy as np
import imutils
import cv2
import serial
import time
x=0 
y=0
r=0
#ser = serial.Serial('/dev/ttyACM0', 9600)
# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (8,100,100)
greenUpper = (28,255,255)
camera = cv2.VideoCapture(0)
time.sleep(1)
count = 0
while True:
	
	ret, frame = camera.read()
	cv2.circle(frame,(325,215), 2, (0,255,0), -1)
	frame = imutils.resize(frame,width=500)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	cv2.imshow("mask",mask)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		# only proceed if the radius meets a minimum size
		if radius > 0:
			# draw the circle and centroid on the frame,
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			x=int(x)
			y=int(y)
			r=int(radius)		
			count=0

			print x,y,r
			output = "X{0:d}Y{1:d}Z{2:d}".format(x,y,r)
			#ser.write(output)
	else:
		count=count+1
		if(count==10):
			x=0
			y=0
			r=0	
			count=0		
			print x,y,r
			output = "X{0:d}Y{1:d}Z{2:d}".format(x,y,r)
			#ser.write(output)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()




