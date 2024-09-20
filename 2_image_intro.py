import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def readImg():
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages','cutepic.jpeg')
    img = cv.imread(imgPath)
    debug = 1
    cv.imshow('Cute Image of a Kitten',img)
    cv.waitKey(0)
    
def writeImg():
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages','cutepic.jpeg')
    img = cv.imread(imgPath)
    outPath = os.path.join(root,'demoImages','cutepicout.png')
    cv.imwrite(outPath, img)

if __name__ == '__main__':
    readImg()
    # writeImg()