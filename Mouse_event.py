import cv2
import numpy as np
# mouse callback function
def draw_circle(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDBLCLK:
      cv2.circle(img,(x,y),1,(255,0,0),1)
     # px = img[x,y]
     # print px
      print x
      print y
      
# Create a black image, a window and bind the function to window
#img = np.zeros((512,512,3), np.uint8)
img=cv2.imread('test5output.png',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
 cv2.imshow('image',img)
 if cv2.waitKey(20) & 0xFF == 27:
  break
cv2.destroyAllWindows()
