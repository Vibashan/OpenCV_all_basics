import cv2
import numpy as np

Face_Cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Eye_Cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(0)
while True:
	_,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	Face =  Face_Cascade.detectMultiScale(gray,1.5,5)

	for x,y,w,h in Face:
		cv2.rectangle( frame ,(x,y),(x+w , y+h), (255,0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		Eye =  Eye_Cascade.detectMultiScale(roi_gray,3,5)
		for ex,ey,ew,eh in Eye:
			cv2.rectangle( roi_color ,(ex,ey),(ex+ew , ey+eh), (0,255,0), 2)

	cv2.imshow("Output",frame)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
