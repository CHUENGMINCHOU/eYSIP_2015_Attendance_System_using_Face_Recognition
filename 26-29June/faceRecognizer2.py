import cv2, os, sys
import numpy as np
from PIL import Image
import serial
import time

ceilingHeight = 180

#filename = "./testVideos/" + sys.argv[1] + ".avi"

camera = cv2.VideoCapture(1)

ser = serial.Serial(
	port='/dev/ttyACM2',
	baudrate=9600
)



def get_training_set(path):
	image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

	images = []
	labels = []

	for image_path in image_paths:

		image = cv2.imread(image_path)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		label = int(image_path[22:24])

		images.append(image)
		labels.append(label)

	return images, labels	
	 
j = 0
detections = [0 for i in range(10)]


def label_to_name(label):
	if label == 1:
			print "Aniket is detected"
	elif label == 2:
			print "Mukesh is detected"
	elif label == 3:
			print "Dheeraj is detected"
	elif label == 4:
			print "Ashish is detected with"
	elif label == 5:
			print "Omkar is detected"
	elif label == 6:
			print "Uttam is detected"
	elif label == 7:
			print "Yousuff is detected"
	elif label == 8:
			print "Kunal is detected"
	elif label == 9:
			print "Chinmay is detected"
	elif label == 10:
			print "Jayanth is detected"

	return

def getHeight():
	if ser.isOpen():
		ser.write('s')
		if ser.inWaiting() > 0:
			temp = ord(ser.read(1))
			print (ceilingHeight - temp)

			return (ceilingHeight - temp)

	#Serial port not open exception
	else:
		return 1000
		
def findMax(array):
	maximum = 0
	i = 1
	while (i < 10):
		if array[i] > array[maximum]:
			maximum = i
		i = i + 1

	return maximum

	
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_recognizer_1 = cv2.createLBPHFaceRecognizer(radius = 1, neighbors= 8, grid_x = 8, grid_y = 8)
face_recognizer_2 = cv2.createLBPHFaceRecognizer(radius = 1, neighbors= 8, grid_x = 8, grid_y = 8)
face_recognizer_3 = cv2.createLBPHFaceRecognizer(radius = 1, neighbors= 8, grid_x = 8, grid_y = 8)

images, labels = get_training_set('./Test3/Range1')
face_recognizer_1.train(images, np.array(labels))

images, labels = get_training_set('./Test3/Range2')
face_recognizer_2.train(images, np.array(labels))

images, labels = get_training_set('./Test3/Range3')
face_recognizer_3.train(images, np.array(labels))

print "System ready"

while(1):

	ret, input_image = camera.read(0)
	if ret == False:
		break

	input_image1 = input_image
	input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
	facesInInputImage = face_cascade.detectMultiScale(input_image, 1.3, 10)

	if len(facesInInputImage) > 0:
		for (x, y, w, h) in facesInInputImage:
			input_image = input_image[y:y+h, x:x+w]
			a, b = input_image.shape
			if a > 0 and b > 0:
				input_image = cv2.resize(input_image, (100, 100) , interpolation = cv2.INTER_CUBIC)						
				cv2.rectangle(input_image1, (x, y), (x+w, y+h), (0,255,0), 3)

				height = getHeight()

				if height < 100:
					continue										
	
				elif height < 126:
					labelDetected, confidence = face_recognizer_1.predict(input_image)

				elif height < 135:
					labelDetected, confidence = face_recognizer_2.predict(input_image)

				else:
					labelDetected, confidence = face_recognizer_3.predict(input_image)
			
				if confidence < 300:
					detections[labelDetected] = detections[labelDetected] + 1													
				
				j = j + 1

				if ( j > 9 ):
					maxDetected = findMax(detections)
					for j in range(10):
						detections[j] = 0
					j = 0

					label_to_name(maxDetected)				

				
	cv2.imshow('image', input_image1)
	
	if cv2.waitKey(1) == 27:
		break



ser.close()
camera.release()
cv2.destroyAllWindows()