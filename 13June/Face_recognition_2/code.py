import cv2, os, sys
import numpy as np
from PIL import Image


def get_training_set(path):
	image_paths = [os.path.join(path, f) for f in os.listdir(path)]

	images = []
	labels = []

	for image_path in image_paths:

		image1 = cv2.imread(image_path)
		image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

		label = int(image_path[15:17])
		images.append(image)
		labels.append(label)
		#faces = face_cascade.detectMultiScale(image, 1.1, 5)

		#for (x, y, w, h) in faces: 
		#		images.append(image[y: y + h, x: x + w])
		#		labels.append(label)

	return images, labels 


def label_to_name(label, confidence):
	if label == 1:
			print "Aniket is detected with confidence {}".format(confidence)
	elif label == 2:
			print "Kevin is detected with confidence {}".format(confidence)
	elif label == 3:
			print "Mukesh is detected with confidence {}".format(confidence)
	elif label == 4:
			print "Chinmay is detected with confidence {}".format(confidence)
	elif label == 5:
			print "Suraj is detected with confidence {}".format(confidence)
	elif label == 6:
			print "Jayant is detected with confidence {}".format(confidence)
	elif label == 7:
			print " Yousuff is detected with confidence {}".format(confidence)
	elif label == 8:
			print "Kunal Jayant Mehta is detected with confidence {}".format(confidence)
	elif label == 9:
			print "Dinesh is detected with confidence {}".format(confidence)
	elif label == 10:
			print "Dheeraj is detected with confidence {}".format(confidence)
	
	return

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

face_recognizer = cv2.createLBPHFaceRecognizer()

images, labels = get_training_set('./FInal')

face_recognizer.train(images, np.array(labels))
cap = cv2.VideoCapture('subject01.avi')
while(cap.isOpened()):
 ret, Frame = cap.read()
 gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
 input_image1 = Frame
 #input_image = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
 facesInInputImage = face_cascade.detectMultiScale(input_image1, 1.25, 10)
 if len(facesInInputImage) > 0:
  for (x, y, w, h) in facesInInputImage:
		input_image = gray[y:y+h, x:x+w]
		#a, b = input_image.shape
		#if a > 0 and b > 0:
		input_image = cv2.resize(input_image, (200, 200), interpolation = cv2.INTER_CUBIC)
		labelDetected, confidence = face_recognizer.predict(input_image)
		cv2.rectangle(input_image, (x, y), (x+w, y+h), (0,255,0), 3)
		label_to_name(labelDetected, confidence)
 cv2.imshow('Video', input_image1)
 if cv2.waitKey(1) == 27:
	break
 		

cap.release()

cv2.destroyAllWindows()







		
