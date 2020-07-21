import cv2
import numpy as np
import time
cam = cv2.VideoCapture(0)
time.sleep(3)
background=0
for i in range(30):
	ret,background = cam.read()
background = np.flip(background,axis=1)
while(cam.isOpened()):
	ret, img = cam.read()
	img = np.flip(img,axis=1)
	print("\t\t\t\tInvisibilisation in progress")
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	value = (35, 35)
	blurred = cv2.GaussianBlur(hsv, value,0)
	
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])
	mask1 = cv2.inRange(hsv,lower_red,upper_red)
	
	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)
	
	mask = mask1+mask2
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	
	img[np.where(mask==255)] = background[np.where(mask==255)]
	cv2.namedWindow('Cloak', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('Cloak', 840,680 )
	cv2.imshow('Cloak',img)
	k = cv2.waitKey(10)
	if k == 27:
		break