import cv2
import numpy as np
from time import sleep

f=[10,41,82,19,95,56,36]
i=0
def nothing(x):
    pass

img=cv2.imread('Naruto.jpg',1)
resized_img=cv2.resize(img,(512,300))
bk = np.full(img.shape, 0, dtype=np.uint8)

#while 1:
      

#cv2.line(img,(0,0),(200,200),(0,0,255),3)

#cv2.circle(img,(55,95),25,(0,255,0),-8)
#cv2.circle(img,(155,125),25,(255,255,0),2)
#kernal= np.ones((5,5) , np.float32)/25
#for i in range(7):
 # cv2.rectangle(img,(f[i],0),(100,100),(255,0,0),3)
 # f.append(i)# if f is an empty array then i will be storing in f
  
#pts=np.array([[56,75],[1,96],[23,156],[79,180],[156,2],[174,12]],np.int32)

#cv2.polylines(img, [pts],True,(255,255,255),2)

#font=cv2.FONT_ITALIC

#cv2.putText(img,'MASSIVE',(100,100),font,1,(0,255,255),2,cv2.LINE_AA)
            
#blur=cv2.GaussianBlur(resized_img, (9,9), 0)# BEST one
cv2.imshow('output',bk)
cv2.imshow('output1',img)


cv2.waitKey(0)
cv2.destroyAllWindows()

