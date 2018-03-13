import cv2
import numpy as np

cap =cv2.VideoCapture(0)
while (cap.isOpened()):
    _,img =cap.read()
    cv2.imshow('output',img)
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
     
    lower_green = np.array([50,120,120])
    upper_green = np.array([80,255,255])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    resg= cv2.bitwise_and(img,img, mask= mask)

    kernal= np.ones((5,5) , np.float32)/25

    smoothed=cv2.filter2D(resg, -1, kernal)
    blur=cv2.GaussianBlur(resg, (5,5), 0)
    #median=cv2.medianBlur(resg, 15)# BEST one

    erosion=cv2.erode(mask,  kernal,  iterations =1)#inside kernal if all are 1 then the
    #middle pixel is one else it will be 0
    dilation=cv2.dilate(mask,  kernal,  iterations =1)# inside kernal if all are 0 then the
    #middle pixel is one else it will be 1
    #erosion and dilation are used continioussly to reduce noise
    opening=cv2.morphologyEx(mask,  cv2.MORPH_OPEN, kernal)#reduce Background noise
    closing=cv2.morphologyEx(mask,  cv2.MORPH_CLOSE ,kernal) #reduce Foreground noise
    median=cv2.medianBlur(closing, 15)# BEST one
    
    cv2.imshow('opening',opening)
    cv2.imshow('resg',resg)
    cv2.imshow('closing',closing)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
                
     

    
    k=cv2.waitKey(10)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
    
