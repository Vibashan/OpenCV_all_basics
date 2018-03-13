#!/usr/bin/env python

import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt

flag=0
pts = deque()
xaxis=deque()
yaxis=deque()
i=0
a=0
b=0

cap = cv2.VideoCapture(1)

while(cap.isOpened()):
    ret, img = cap.read()

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
      
    lower_blue = np.array([83,120,120],np.uint8)
    upper_blue = np.array([170,255,255],np.uint8)
    blue=cv2.inRange(hsv, lower_blue, upper_blue)
    _,contours,h = cv2.findContours(blue,1,2)


    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        pts.appendleft(center)
        if flag==0:
            a,b=center                       
            flag+=1
                
        else:
            c,d=center
            x= math.sqrt((c-a)(c-a)+(d-b)(d-b))/2.0
            x=x/37.795    #37.795 for pixels to cm
            a=c
            b=d
            i+=2
            m,n=pts[-1]
            for i in xrange(1, len(pts)):              
                cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255),2)
    
            y=math.sqrt((c-m)(c-m)+(d-n)(d-n))
            xaxis.append(y)
            yaxis.append(i)
                 
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
 
    if key == ord("q"):
        break
    yaxis.appendleft(0)
    xaxis.appendleft(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
