import cv2
import numpy as np

def face_detector(image):
    face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')
    # Check if the face cascade file has been loaded
    if face_cascade.empty():
        raise IOError('Unable to load the face cascade classifier xml file')


    img = cv2.imread(image)
    scaling_factor = 0.5
    img = cv2.resize(img, (0,0), fx=scaling_factor, fy=scaling_factor)

    face_rects = face_cascade.detectMultiScale(img, 1.3, 5)

    # Draw rectangles on the image
    for (x,y,w,h) in face_rects:
        print(x , y , w , h)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)    

    cv2.imwrite(image, img)
