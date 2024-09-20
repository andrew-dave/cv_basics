#Here we segment a cat from its original image using HSV segmentation and overlaying the mask on the original image

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

    # Define the HSV range for color segmentation(for body and ~eyes)
    lowerBound = np.array([10, 100, 100])
    upperBound = np.array([25, 255, 255])

    # Segment red regions
    # lowerBound = np.array([0, 120, 70])
    # upperBound = np.array([10, 255, 255])
    
    # Segment green regions
    # lowerBound = np.array([35, 100, 100])
    # upperBound = np.array([85, 255, 255])

    # Create mask
    mask = cv.inRange(imgHSV, lowerBound, upperBound)

    # Apply the mask to the original image to visualize the segmentation
    result = cv.bitwise_and(imgRGB, imgRGB, mask=mask)

    # Display original image
    plt.figure()
    plt.imshow(imgRGB)
    plt.title("RGB Image")
    plt.show()

    # Display the mask
    cv.imshow("Mask", mask)

    # Display the segmented image
    plt.figure()
    plt.imshow(result)
    plt.title("Segmented Image")
    plt.show()

    # Close OpenCV windows
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    hsvColorseg()
