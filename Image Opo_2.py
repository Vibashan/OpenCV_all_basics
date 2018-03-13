import cv2
import numpy as np

img1=cv2.imread('Angrybird.png')
img2=cv2.imread('Python.png')

#add=cv2.add(img1,img2)  ADD ALL PIXELS
#weightedadd=cv2.addWeighted(img1,0.8,img2,.3,0)
cv2.imshow('real_img1',img1)
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,  roi,  mask=mask_inv)
cv2.imshow('roi',roi)
img2_fg=cv2.bitwise_and(img2,  img2,  mask=mask)

dst=cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols]= dst


cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('mask',mask)

cv2.imshow('img1',img1)





cv2.waitKey(0)
