############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read & Resize the image
img = cv2.imread('sk.png')
height, width, channels = img.shape
img1 = cv2.resize(img,(width, height/2), interpolation = cv2.INTER_CUBIC)
############################################

############################################
## Do the processing
change2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(change2gray,50,255,0)
contour,hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img1,contour,-1,(0,0,255),1)


for cnt in contour:
    ma = np.zeros(change2gray.shape,np.uint8)
    cv2.drawContours(ma,[cnt],0,255,-1)
    mean = cv2.mean(img1,ma)
    print mean


print len(contour)
moments =cv2.moments(cnt)
print moments
############################################

############################################
## Show the image
cv2.imshow('image',img1)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
