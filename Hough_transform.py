import cv2
import numpy as np

img = cv2.imread('Angrybird.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,150,apertureSize = 3)#2nd and 3rd argument are minVal and maxVal

cv2.imshow('lines',edges)

cv2.waitKey(10000)

lines = cv2.HoughLines(edges,1,np.pi/180,10) #4th argument is threshold(Or minimum no of vote it should get to be considered as a line)
"""
Probabilistic Hough Transform
#Here it gives only the Start and End point so its more efficient.(best one to use and less computation)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

Hough Circles are alao possible
"""

for rho,theta in lines[0]:
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('houghlines3',img)

cv2.waitKey(10000)