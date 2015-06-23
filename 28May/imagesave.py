import numpy as np
import cv2
img = cv2.imread('t.jpeg',1)
cv2.imshow('t',img)
k=cv2.waitKey(0)
if k==27:
 cv2.destroyAllWindows()
elif k == ord('s'):
 cv2.imwrite('t.png',img)
 cv2.destroyAllWindows()
