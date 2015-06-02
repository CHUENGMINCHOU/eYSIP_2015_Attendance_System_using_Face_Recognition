import numpy as np
import cv2
img1 = cv2.imread('starry_night.jpg')
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('starry_night',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

