import os
import cv2
import numpy as np

filelist = os.listdir('.')  # get files in current directory
i=1
for filename in filelist:
    if ".jpeg" in filename:  # only process pictures
	newname = "subject08_" + str(i) + ".jpeg"
        img1 = cv2.imread(newname)
	img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	height, width = img2.shape[:2]
	res = cv2.resize(img2,(width/2, height/2), interpolation = cv2.INTER_CUBIC)
	cv2.imwrite(newname,res)
	i=i+1


cv2.waitKey(0)
cv2.destroyAllWindows()
