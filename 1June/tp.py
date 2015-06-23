import cv2
import cv2.cv as cv
import getopt, sys

def detect(img, cascade):
    for scale in [float(i)/10 for i in range(11, 15)]:
        for neighbors in range(2,5):
            rects = cascade.detectMultiScale(img, scaleFactor=scale, minNeighbors=neighbors,
                                             minSize=(20, 20), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

            print 'scale: %s, neighbors: %s, len rects: %d' % (scale, neighbors, len(rects))


def find_face_from_img(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = detect(gray, cascade)


if __name__ == '__main__':

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try: video_src = video_src[0]
    except: video_src = 0
    args = dict(args)

    c=cv2.VideoCapture(0)
    cascade_fn = args.get('--cascade', "cascades/haarcascade_frontalface_alt.xml")
    cascade = cv2.CascadeClassifier(cascade_fn)

    gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
    
    faces = cascade.detectMultiScale(gray, 1.05, 5)
    while(1):
        ret, frame = c.read()
	cv2.imshow("images",frame)
       # rects = find_face_from_img(frame)
	for (x,y,w,h) in faces:
 		cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
 		roi_gray = gray[y:y+h, x:x+w]
 		roi_color = img1[y:y+h, x:x+w]
        if 0xFF & cv2.waitKey(5) == 27:
                break

cv2.destroyAllWindows()
