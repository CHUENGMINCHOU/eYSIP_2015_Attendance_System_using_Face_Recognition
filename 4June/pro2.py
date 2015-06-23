import cv2, os, sys
import numpy as np
from PIL import Image


def get_training_set(path):
	image_paths = [os.path.join(path, f) for f in os.listdir(path)]

	images = []

	for image_path in image_paths:

		image1 = cv2.imread(image_path)
		image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
		images.append(image)
		
	return images

filelist = os.listdir('.')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


input_image = cv2.imread(sys.argv[1])
input_image1 = input_image
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
facesInInputImage = face_cascade.detectMultiScale(input_image, 1.3, 10)
i=01
for filename in filelist:
	if "subject_" in filename:  # only process pictures
		newname = "subject_" + str(i) + ".jpg"
		for (x, y, w, h) in facesInInputImage:
			input_image = input_image[y:y+h, x:x+w]
			input_image = cv2.resize(input_image, (200, 200), interpolation = cv2.INTER_CUBIC)
			cv2.rectangle(input_image, (x, y), (x+w, y+h), (0,255,0), 3)
			cv2.imwrite(newname,input_image)
		i=i+1
cv2.imshow(input_image, input_image)

cv2.waitKey(0)

cv2.destroyAllWindows()





    if "subject_" in filename:  # only process pictures
        newname = "subject_" + str(i) + ".jpg"
        print(filename + " will be renamed as " + newname)
	i=i+1
        os.rename(filename, newname)
