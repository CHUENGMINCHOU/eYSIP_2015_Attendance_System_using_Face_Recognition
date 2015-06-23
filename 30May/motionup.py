import os, sys
import cv2
cap = cv2.VideoCapture(1)
ret, frame = cap.read()
g_old = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
h,w = g_old.shape
imgt1 = cv2.resize(g_old,(w/5,h/5), interpolation = cv2.INTER_AREA)
while(True):
 ret, frame = cap.read()
 g_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 imgt2 = cv2.resize(g_new,(w/5,h/5), interpolation = v2.INTER_AREA)
 img_diff = cv2.absdiff(imgt2,imgt1)
 cv2.imshow('Result',img_diff)
 if cv2.countNonZero(imgt_diff) > 2000:
  print('yo whats up')
  gray_new = gray_old
 if cv2.waitKey(1)==27:
  break
cap.release()
cv2.destroyAllWindows()
