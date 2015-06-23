import cv2, os, sys

def facechop(input_image):  
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(input_image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)


    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
	change =cv2.resize(sub_face, (200, 200), interpolation = cv2.INTER_CUBIC)
	change1 =cv2.cvtColor(change,cv2.COLOR_BGR2GRAY)
        face_file_name = "face_" + str(y) + ".jpeg"
        cv2.imwrite(face_file_name, change1)

    cv2.imshow(image, img)

    return

if __name__ == '__main__':  
    input_image = cv2.imread(sys.argv[1])
    facechop(input_image)

    while(True):
        key = cv2.waitKey(20)
        if key in [27, ord('Q'), ord('q')]: 
            break
