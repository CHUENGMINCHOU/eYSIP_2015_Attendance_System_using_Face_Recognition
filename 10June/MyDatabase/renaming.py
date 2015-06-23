#The folder of images should also contain a text file containing names of all the images in the folder.

#Parameters : 1. Name of the folder 
#			  2. Number of the subject

import cv2
import numpy as np
import os
import os.path
import sys

os.chdir("./" + sys.argv[1])
f = open("Images.txt", "r")

n = len([name for name in os.listdir('.') if os.path.isfile(name)])

i=0

while i < n-1:
	image=f.readline()
	image1=image[0:(len(image) - 1)]	
	newName = "subject"+ sys.argv[2] + "_" + str(i)+".jpg"	
	os.rename(image1, newName)
	i=i+1

f.close()
