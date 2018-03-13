import cv2
import numpy as np

img=cv2.imread('Angrybird.png',1)

#img[100:120,100:150]=(255,255,255)

#img[0:60,0:100]=img[110:170,30:130]

rows,cols,channels=img.shape
blank_image = np.zeros((rows,cols,3), np.uint32)
img1 = cv2.resize(img,(28,28))
cv2.imwrite("4/0.png",img1)

px = img[0,10]
print px
blue = img[0,10,0]
print blue
red = img[0,10,2]
print red

img.itemset((0,10,2),100)#modifying RED value

print img.shape
b,g,r = cv2.split(img)# store all blue pixel value in b and respectively
img[:,:,2] = 0#making red pixel all 0

cv2.namedWindow('Output', cv2.WINDOW_NORMAL)
#cv2.namedWindow('Output', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Output',img)
cv2.imshow('blank_image',blank_image)
#cv2.imwrite('messigray.png',img)


cv2.waitKey(0)
cv2.destroyAllWindows(0)
