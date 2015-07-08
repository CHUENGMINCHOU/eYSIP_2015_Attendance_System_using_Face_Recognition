import cv2
import numpy as np
from PIL import Image
import os
import sys
import serial 
import time
from mySerial import *

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_recognizer_1 = cv2.createLBPHFaceRecognizer(radius = 1, neighbors= 8, grid_x = 8, grid_y = 8)
face_recognizer_2 = cv2.createLBPHFaceRecognizer(radius = 1, neighbors= 8, grid_x = 8, grid_y = 8)
face_recognizer_3 = cv2.createLBPHFaceRecognizer(radius = 1, neighbors= 8, grid_x = 8, grid_y = 8)

'''	
ser = serial.Serial(
	port='/dev/ttyACM0',
	baudrate=9600
)
'''

#This function takes the path to the directory containing the training the 
#training images and returns two lists: one containing the faces and the other 
#list containing the corresponding labels.
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


#This function initializes resources and trains the recognizers 
def init_recognizer():
	images, labels = get_training_set('./Test3/Range1')
	face_recognizer_1.train(images, np.array(labels))

	images, labels = get_training_set('./Test3/Range2')
	face_recognizer_2.train(images, np.array(labels))

	images, labels = get_training_set('./Test3/Range3')
	face_recognizer_3.train(images, np.array(labels))

	print "System ready"

'''
def getHeight():
    
    return 230
    if ser.isOpen():
        ser.write('s')
        if ser.inWaiting() > 0:
            temp = ord(ser.read(1))
            print (ceilingHeight - temp)

            return (ceilingHeight - temp)

	#Serial port not open exception
    else:
        return 1000
'''

#This functions returns the label of the person detected in the image.
#If no person is detected, label returned is 100
#If no person is recognized, label returned is 200
def get_label_2(input_image):
    cv2.imwrite("image.jpg", input_image)
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(input_image, 1.3, 10)
    
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            input_image = input_image[y:y+h, x:x+w]
            a, b = input_image.shape
            if a > 0 and b > 0:
                height = getHeight()

                if height < 100 or height > 150:
                    continue										
	
                elif height < 126:
                    labelDetected, confidence = face_recognizer_1.predict(input_image)

                elif height < 135:
                    labelDetected, confidence = face_recognizer_2.predict(input_image)

                elif height < 150:
                    labelDetected, confidence = face_recognizer_3.predict(input_image)
				
               
                if confidence < 300:
                    return labelDetected

                else:
                    return 11												
		
        return 0

    else:         
        return 0


#This function takes as input a label and returns the name of the person corresponding
#to that label
def label_to_name(label):
    if label == 1:
        return "Aniket"
    
    elif label == 2:
        return "Mukesh"
    
    elif label == 3:
        return "Dheeraj"
    
    elif label == 4:
        return "Ashish"
    
    elif label == 5:
        return "Omkar"
    
    elif label == 6:
        return "Uttam"
    
    elif label == 7:
        return "Yousuff"
    
    elif label == 8:
        return "Kunal"
    
    elif label == 9:
        return "Chinmay"
    
    elif label == 10:
        return "Jayanth"
   


 
