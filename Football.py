
import Rpi.GPIO as GPIO
import numpy as np
import imutils
import cv2
import serial
import time

lf = 16
lb = 18
en1 = 22
rf = 23
rb = 21
en2 = 19

GPIO.setup(lf,GPIO.OUT)
GPIO.setup(lb,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(rf,GPIO.OUT)
GPIO.setup(rb,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

def straight():

 GPIO.output(lf,GPIO.HIGH)
 GPIO.output(lb,GPIO.LOW)
 GPIO.output(en1,GPIO.HIGH)
 GPIO.output(rf,GPIO.HIGH)
 GPIO.output(rb,GPIO.LOW)
 GPIO.output(en2,GPIO.HIGH)


def back():

 GPIO.output(lf,GPIO.LOW)
 GPIO.output(lb,GPIO.HIGH)
 GPIO.output(en1,GPIO.HIGH)
 GPIO.output(rf,GPIO.LOW)
 GPIO.output(rb,GPIO.HIGH)
 GPIO.output(en2,GPIO.HIGH)

def left():

 GPIO.output(lf,GPIO.LOW)
 GPIO.output(lb,GPIO.HIGH)
 GPIO.output(en1,GPIO.HIGH)
 GPIO.output(rf,GPIO.HIGH)
 GPIO.output(rb,GPIO.LOW)
 GPIO.outpu(en2,GPIO.HIGH)

def right():
 
 GPIO.output(lf,GPIO.HIGH)
 GPIO.output(lb,GPIO.LOW)
 GPIO.output(en1,GPIO.HIGH)
 GPIO.output(rf,GPIO.LOW)
 GPIO.output(rb,GPIO.HIGH)
 GPIO.output(en2,GPIO.HIGH)

def stop():

 GPIO.output(lf,GPIO.LOW)
 GPIO.output(lb,GPIO.LOW)
 GPIO.output(en1,GPIO.LOW)
 GPIO.output(rf,GPIO.LOW)
 GPIO.output(rb,GPIO.LOW)
 GPIO.output(en2,GPIO.LOW)

 
#ser = serial.Serial('/dev/ttyACM0', 9600)
# define the lower and upper boundaries of the "ball"
# ball in the HSV color space, then initialize the
# list of tracked points
ballLower = (8,100,100)
ballUpper = (28,255,255)
camera = cv2.VideoCapture(1)
time.sleep(1)
count = 0
while True:
	
	ret, frame = camera.read()
	cv2.circle(frame,(325,215), 2, (0,255,0), -1)
	frame = imutils.resize(frame,width=500)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, ballLower, ballUpper)
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
			if x<270&&x>230:
				straight()
			elif x>270:
				right()
			elif x<230:
				left()
			
	else:
		count=count+1
		if(count==5):
			x=0
			y=0
			r=0	
			count=0		
			right()
			time.sleep(2)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()
