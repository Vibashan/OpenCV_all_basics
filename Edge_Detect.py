import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	solbelx = cv2.Sobel(frame, cv2.CV_64F,1,0,ksize=5)
	solbely = cv2.Sobel(frame, cv2.CV_64F,0,1,ksize=5)
	canny = cv2.Canny(frame,100,200)#As number increase the Sharp edges will remian	
	
	cv2.imshow("Output",laplacian)
	cv2.imshow("Input",frame)
	cv2.imshow("solbelx",solbelx)
	cv2.imshow("solbely",solbely)
	cv2.imshow("canny",canny)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()

