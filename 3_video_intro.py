import numpy as np
import cv2 as cv
import os

def videoCapture():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()
    while(True):
        ret, frame = cap.read()
        if ret:
            cv.imshow('Webcam from phone', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def videoFromfile():
    root = os.getcwd()
    vidPath = os.path.join(root, 'demoImages', 'cutecat.mp4')
    cap = cv.VideoCapture(vidPath)
    
    if not cap.isOpened():
        exit()
    
    while(True):
        ret, frame = cap.read()
        cv.imshow('Video',frame)
        cv.resizeWindow('Video', 540, 960)  # Adjust the size here

        delay = int(1000/60)
        
        if cv.waitKey(delay) == ord('q'):
            break

def writeVideotofile():
    cap = cv.VideoCapture(0)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    root = os.getcwd()
    outpath = os.path.join(root, 'demoImages', 'webcam.avi')
    
    out = cv.VideoWriter(outpath, fourcc, 24, (640,480))

    if not cap.isOpened():
        exit()
    
    while(True):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow('Webcam video', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ =='__main__':
    # videoCapture()
    # videoFromfile()
    writeVideotofile()