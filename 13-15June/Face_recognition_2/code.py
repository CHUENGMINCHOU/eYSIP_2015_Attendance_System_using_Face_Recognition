import cv2, os,sys
import numpy as np

def Get_training_set(Path):
    Image_paths = [os.path.join(Path, f) for f in os.listdir(Path)]
    Images = []
    Labels = []
    for Image_path in Image_paths:
        Image1 = cv2.imread(Image_path)
        Image = cv2.cvtColor(Image1, cv2.COLOR_BGR2GRAY)
        Label = int(Image_path[15:17])
        Images.append(Image)
        Labels.append(Label)
    return Images, Labels

def Label_to_name(Label, Confidence):
    if Label == 1:
        print "Aniket is detected with confidence {}".format(Confidence)
    elif Label == 2:
        print "Mukesh is detected with confidence {}".format(Confidence)
    elif Label == 3:
        print "Dheeraj is detected with confidence {}".format(Confidence)
    elif Label == 4:
        print "Ashish is detected with confidence {}".format(Confidence)
    elif Label == 5:
        print "Omkar is detected with confidence {}".format(Confidence)
    elif Label == 6:
        print "Jayant is detected with confidence {}".format(Confidence)
    elif Label == 7:
        print " Yousuff is detected with confidence {}".format(Confidence)
    elif Label == 8:
        print "Kunal Jayant Mehta is detected with confidence {}".format(Confidence)
    elif Label == 9:
        print "Chinmay is detected with confidence {}".format(Confidence)
    elif Label == 10:
        print "Jayant is detected with confidence {}".format(Confidence)
    return

Face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
Face_recognizer = cv2.createLBPHFaceRecognizer()
Images, Labels = Get_training_set('./FInal')
Face_recognizer.train(Images, np.array(Labels))
Cap = cv2.VideoCapture('subject04.avi')
while Cap.isOpened():
    Ret, Frame = Cap.read()
    Gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    Input_image1 = Frame
    FacesInInputImage = Face_cascade.detectMultiScale(Input_image1, 1.25, 10)
    if len(FacesInInputImage) > 0:
        for (x, y, w, h) in FacesInInputImage:
            Input_image = Gray[y:y+h, x:x+w]
            Input_image = cv2.resize(Input_image, (200, 200), interpolation = cv2.INTER_CUBIC)
            LabelDetected, Confidence = Face_recognizer.predict(Input_image)
            cv2.rectangle(Input_image, (x, y), (x+w, y+h), (0,255,0), 3)
            Label_to_name(LabelDetected, Confidence)
            cv2.imshow('Video', Input_image1)
    if cv2.waitKey(1) == 27:
        break

Cap.release()
cv2.destroyAllWindows()
