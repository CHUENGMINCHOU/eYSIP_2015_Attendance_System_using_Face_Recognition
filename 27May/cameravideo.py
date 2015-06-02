import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
 ret, Frame = cap.read()
 gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
 cv2.imshow('Frame',gray)
 if cv2.waitKey(1) == 27:
  break

cap.release()
cv2.destroyAllWindows()
