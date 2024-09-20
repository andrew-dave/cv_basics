# Basic understanding of HSV colour segments 
import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def hsvColorseg():
    root = os.getcwd()
    imgpath = os.path.join(root, 'demoImages','cutepic.jpeg')
    img  = cv.imread(imgpath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowerBound = np.array([0,0,50])
    upperBound = np.array([150,140,180])

    mask = cv.inRange(imgHSV, lowerBound, upperBound)

    plt.figure()
    plt.imshow(imgRGB)
    plt.title("RGB")
    plt.show()
    # plt.subplot(232)
    # plt.imshow(imgHSV)
    # plt.title("HSV")
    cv.imshow("mask", mask)
    cv.waitKey(0)



if __name__ == '__main__':
    hsvColorseg()