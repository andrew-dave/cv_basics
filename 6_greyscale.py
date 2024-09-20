# Obtaining the scaled values of each channel within a color image
# each greyscale pixel = 0.299*R + 0.587*G + 0.133*B
import cv2 as cv
import os

def greyScale():
    root = os.getcwd()
    imgpath = os.path.join(root,"demoImages", "cutepic.jpeg")
    img = cv.imread(imgpath)
    imGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('Gray',imGray)
    cv.waitKey(0)
    cv.destroyAllWindows()

def readasGrey():
    root = os.getcwd()
    imgpath = os.path.join(root,"demoImages", "cutepic.jpeg")
    img = cv.imread(imgpath, cv.IMREAD_GRAYSCALE)

    cv.imshow('Gray',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    # greyScale()
    readasGrey()