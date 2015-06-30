import numpy
import cv2
import sys

camera = cv2.VideoCapture(1)

i = 0

while(1):
	ret, image = camera.read(0)
	cv2.imshow('image', image)
	k = cv2.waitKey(1)
	print k
	if k==27:
		break
	elif k == 99:
		cv2.imwrite(sys.argv[1] + "_" + str(i) + ".jpg", image)
		i = i+1

cap.release()
cv2.destroyAllWindows()

