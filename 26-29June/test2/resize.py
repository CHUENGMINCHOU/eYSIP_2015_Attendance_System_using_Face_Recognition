import os
import sys
import cv2
import numpy

images = [image for image in os.listdir('.') if image.endswith('.jpg')]

for image in images:
	original = cv2.imread(image)
	res = cv2.resize(original,(200,200), interpolation = cv2.INTER_CUBIC)
	os.chdir('./resized')
	cv2.imwrite(image, res)
	os.chdir('..')


