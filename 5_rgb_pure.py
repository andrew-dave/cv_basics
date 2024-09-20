import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def pureColors():
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))
    bImg = cv.merge((zeros,zeros, 255*ones))
    gImg = cv.merge((zeros,255*ones, zeros))
    rImg = cv.merge((255*ones,zeros, zeros))
    black_img = cv.merge((zeros,zeros,zeros))
    white_img = cv.merge((255*ones,255*ones,255*ones))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('Blue')
    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('Green')
    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('Red')
    plt.subplot(234)
    plt.imshow(black_img)
    plt.title('Kuroi')
    plt.subplot(235)
    plt.imshow(white_img)
    plt.title('Shiroi')

    plt.show()

def bgr_greyscalechannel():
    root = os.getcwd()
    imgpath = os.path.join(root, 'demoImages','cutepic.jpeg')
    img = cv.imread(imgpath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    b,g,r = cv.split(img)

    plt.figure()
    plt.subplot(231)
    plt.imshow(imgRGB)
    plt.title('OG')
    plt.subplot(232)
    plt.imshow(b, cmap='grey')
    plt.title("Blue")
    plt.subplot(233)
    plt.imshow(g, cmap='grey')
    plt.title("Green")
    plt.subplot(234)
    plt.imshow(r, cmap='grey')
    plt.title("Red")
    

    plt.show()

def bgrChannelcolor():
    root = os.getcwd()
    imgpath = os.path.join(root, 'demoImages','cutepic.jpeg')
    img = cv.imread(imgpath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    b,g,r = cv.split(img)

    zeros = np.zeros_like(g)
    bimg = cv.merge((b, zeros,zeros))
    gimg = cv.merge((zeros, g,zeros))
    rimg = cv.merge((zeros, zeros,r))
    
    plt.figure()
    plt.subplot(131)
    plt.imshow(bimg)
    plt.subplot(132)
    plt.imshow(gimg)
    plt.subplot(133)
    plt.imshow(rimg)
    plt.show()
    h,w,d = img.shape
    print(f"Height: {h}, Width: {w}, Depth: {d}")
if __name__ =='__main__':
    # pureColors()
    # bgr_greyscalechannel()
    bgrChannelcolor()