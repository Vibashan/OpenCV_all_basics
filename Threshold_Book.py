import  cv2
import numpy as np

img=cv2.imread('Bookpage.jpg',1)

retval,threshold= cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold2=cv2.threshold(gray, 10, 255,cv2.THRESH_BINARY)

gaus=cv2.adaptiveThreshold(gray,  255,  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  cv2.THRESH_BINARY, 115, 1)
       

cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gaus',gaus)
cv2.imshow('img',img)

cv2.waitKey(0)
