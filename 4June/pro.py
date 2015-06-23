import cv2, os, sys
import numpy as np
from PIL import Image

image = cv2.imread(sys.argv[1])
height, width, c= image.shape
input_image = cv2.resize(image, (width/8, height/8), interpolation = cv2.INTER_CUBIC)
input_image1 = image
input_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#facesInInputImage = face_cascade.detectMultiScale(input_image, 1.3, 10)

#for (x, y, w, h) in facesInInputImage:
#input_image = input_image[y:y+h, x:x+w]
input_image = cv2.resize(input_image, (200, 200), interpolation = cv2.INTER_CUBIC)
cv2.imwrite('kevin.jpg', input_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

	
