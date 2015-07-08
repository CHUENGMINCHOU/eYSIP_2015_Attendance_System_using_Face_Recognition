import os
import sys
import cv2
import numpy

image = sys.argv[1]
sizex = int(sys.argv[2])
sizey = int(sys.argv[3])

original = cv2.imread(image)
res = cv2.resize(original, (sizex,sizey), interpolation = cv2.INTER_CUBIC)

cv2.imwrite(image + "_copy", res)



