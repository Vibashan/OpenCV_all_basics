import cv2
import numpy as np

img=cv2.imread('Naruto.jpg',1)
for i in range(99):
      for j in range(99):
            b=img[i,j,0]
            g=img[i,j,1]
            r=img[i,j,2]
            if( b>g and b>r ):
                  b=255
                  r=0
                  g=0
            if (g>r and  g>b) :
                  g=255
                  r=0
                  b=0
            if (r>g and r>b) :
                  r=255
                  g=0
                  b=0
            img[i,j]=(b,g,r)
      
cv2.imshow('Output',img)

cv2.waitKey(0)
