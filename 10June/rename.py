#Pass the number of images in the folder as the argument while running the script.
#This file should be in the same directory as the images 
#The directory should also contain a text file containing names of all the images in the directory.

import cv2
import numpy as np
import os
import sys

f = open("Images.txt", "r")

i=0

while i < sys.argv[2]:
	image=f.readline()
	image1=image[0:(len(image) - 1)]	
	newName = "subject"+ sys.argv[1] + "_" + str(i)+".jpeg"	
	os.rename(image1, newName)
	i=i+1

f.close()
