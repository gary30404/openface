#!/usr/bin/env python2
import cv2
import numpy as np
from PIL import Image
from threading import Timer
import time
import os
#value = 1
#img = cv2.imread('IMG_4244.jpg')
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#print(hsv[:,:,2])
#hsv+=255
#print(len(hsv))
#v = hsv[:,:,2]
#print(len(v))
#s = np.mean(v)
#s = s/255
#print(s)
#s = s/np.mean(hsv)
#print(s)
#img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#cv2.imwrite("image_processed.jpg", img)
#name = raw_input()
name = 'test'
directory = '/Users/gary/openface/demos/web/data/training_data/'+name+'/'
if not os.path.exists(directory):
    os.makedirs(directory)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
# Define the codec and create VideoWriter object
#fourcc = cv2.cv.CV_FOURCC(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
i = 1
sec = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        frameshow = frame
        #out.write(frame)
        cv2.putText(frameshow, "{:}".format(sec), (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.75,
                    color=(152, 255, 204), thickness=2)
        cv2.imshow('frame', frameshow)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if i % 20 == 0:
            sec=sec+1
            cv2.imwrite(directory+str(sec)+'.jpg', frame)
        i=i+1
        if sec == 45:
            break
    else:
        break
cap.release()
#out.release()
#cv2.destroyAllWindows()

for indx, f in enumerate(os.listdir(directory), start=1):
    image = cv2.imread(directory+f)
    cv2.imshow("Image-{}".format(indx), image)
    while(True):
        if cv2.waitKey(1) & 0xFF == ord('n'):
            break
        if cv2.waitKey(1) & 0xFF == ord('d'):
            os.remove(directory+f)
            break
