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
def move_robot(x,y):
	if x > 250:
		left()
		print 'Turning left'
	elif x < 250:
		right()
		print 'Turning right'
	else:
		straight()
		print 'Moving Forward'
'''
def robot_turnleft():
	print 'Turning Left'
	
def robot_turnright():
	print 'Turning Right'
'''
def robot_slideleft():
	print 'Sliding Left'
	left()
	time.sleep(0.5)
	straight()
	time.sleep(0.5)
	right()
	time.sleep(0.5)

def robot_slideright():
	print 'Sliding Right'
	right()
	time.sleep(0.5)
	straight()
	time.sleep(0.5)
	left()
	time.sleep(0.5)

def robot_shoot():
	print 'Shooting Ball'

def robot_gatherball(x,y,ti):
	print 'Gathering Ball'
	time.sleep(5)
	print x,y,ti
	
def rotate():
	right()
	time.sleep(0.5)
	stop()
	

def find_soccerball():
	print 'Finding Soccer Ball'

def soccer_ball(frame):
	greenLower = (8,100,100)
	greenUpper = (28,255,255)

	cv2.circle(frame,(325,215), 2, (0,255,0), -1)
	frame = imutils.resize(frame,width=500)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, greenLower, greenUpper)
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
			return True, x,y,r
	else:

			x=0
			y=0
			r=0	
			count=0	
			return False, x,y,r	

def ball_detect(frame,greenLower,greenUpper):

	cv2.circle(frame,(325,215), 2, (0,255,0), -1)
	frame = imutils.resize(frame,width=500)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, greenLower, greenUpper)
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
			return True, x,y,r
	else:
			x=0
			y=0
			r=0	
			count=0	
			return False, x,y,r	


def shoot_ball():

	print 'GOAL'
	b = 1000
	output = "Y{1:d}".format(b)
	#ser.write(output)


import numpy as np
import imutils
import cv2
import serial
import time
import Rpi.GPIO as GPIO

#ser = serial.Serial('/dev/ttyACM0', 9600)
cam = cv2.VideoCapture(0)
count = 0
hsvSoccerLow = (8,100,100)
hsvSoccerUp = (28,255,255)
hsvGoalLow = (8,100,100)
hsvGoalUp = (28,255,255)
proto_1 = True
proto_2 = False
while True:
	count = count + 1
	_,frame = cam.read()
	if proto_1 is True: #find soccer ball
		print 'Protocol 1'
		s_ball,x,y,r = ball_detect(frame,hsvSoccerLow,hsvSoccerUp)
		if s_ball:
			print 'Found Ball'
			move_robot(x,y)
			if r > 50:
				robot_gatherball(x,y,3)
				proto_1 = False
				proto_2 = True
			print x,y,r
		else:
			if count%20 == 0:
				print 'Turning Around'
				rotate()
			

	elif proto_2 is True: #Soccer Ball is captured, searching for Goal	
		print 'Protocol 2'
		g_ball,x,y,r = ball_detect(frame,hsvGoalLow,hsvGoalUp)
		if g_ball is True:
			print 'Found Goal'
			move_robot(x,y)
			if r > 60:
				x_true = x #x value of goal post
				time.sleep(3)
				sm,x_small,y_small,r_small = ball_detect(frame,hsvSoccerLow,hsvSoccerUp)
				print x_small,x_true
				diff_x = x_true-x_small
				print diff_x
				if diff_x >5:
					robot_slideleft()
				elif diff_x<5:
					robot_slideright()
				else:
					shoot_ball()
					time.sleep(10)
					proto_1 = True


					proto_2 = False 

		else:	
			if count%20 == 0:
				print 'Turning Around'
				rotate()
				
	cv2.imshow('Camera',frame)
	cv2.waitKey(5)





	
