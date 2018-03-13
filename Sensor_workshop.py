import cv2
import numpy as np

Face_Cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Eye_Cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def blend_transparent(face_img, overlay_t_img):
    # Split out the transparency mask from the colour info
    overlay_img = overlay_t_img[:,:,:3] # Grab the BRG planes
    overlay_mask = overlay_t_img[:,:,3:]  # And the alpha plane

    # Again calculate the inverse mask
    background_mask = 255 - overlay_mask

    # Turn the masks into three channel, so we can use them as weights
    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    # Create a masked out face image, and masked out overlay
    # We convert the images to floating point in range 0.0 - 1.0
    face_part = (face_img * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    # And finally just add them together, and rescale it back to an 8bit integer image    
    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))

cap = cv2.VideoCapture(0)
Dog = cv2.imread('Krrish.png',-1)

while True:
	_,img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	Face =  Face_Cascade.detectMultiScale(gray,1.5,5)

	for x,y,w,h in Face:
		#cv2.rectangle( frame ,(x,y),(x+w , y+h), (255,0,0), 2)
		overlay_image = cv2.resize(Dog,(w,h))
	        img[y:y+h,x:x+w,:] = blend_transparent(img[y:y+h,x:x+w,:], overlay_image)
		#roi_gray = gray[y:y+h, x:x+w]
		#roi_color = frame[y:y+h, x:x+w]
		#Eye =  Eye_Cascade.detectMultiScale(roi_gray,3,5)
		#for ex,ey,ew,eh in Eye:
		#	cv2.rectangle( roi_color ,(ex,ey),(ex+ew , ey+eh), (0,255,0), 2)

	cv2.imshow("Output",img)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
