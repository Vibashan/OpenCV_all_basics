import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDBLCLK:
      cv2.circle(hsv,(x,y),1,(255,0,0),1)
      px = hsv[x,y]
      print px
      

img=cv2.imread('Naruto.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
 cv2.imshow('image',hsv)
 if cv2.waitKey(20) & 0xFF == 27:
  break
cv2.destroyAllWindows()
