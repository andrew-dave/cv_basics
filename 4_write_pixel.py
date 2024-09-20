import os
import cv2 as cv
import matplotlib.pyplot as plt

def readwritepixel():
    root = os.getcwd()
    imgpath = os.path.join(root, 'demoImages', 'cutepic.jpeg')
    img = cv.imread(imgpath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    eyepixel = imgRGB[230,280]
    imgRGB[230,280] = (250, 150, 0)
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

def readwritepixelRegion():
    root = os.getcwd()
    imgpath = os.path.join(root, 'demoImages', 'cutepic.jpeg')
    img = cv.imread(imgpath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    eyeRegion = imgRGB[227:264, 164:204]
    
    [heye, weye] = eyeRegion.shape[:2]
    center = [weye//2,heye//2]
    angle = 30
    scale = 1.0
    r_mat = cv.getRotationMatrix2D(center, angle, scale)
    rot_eye = cv.warpAffine(eyeRegion, r_mat, (weye,heye), borderMode=cv.BORDER_REPLICATE)

    dy = 204-164
    dx = 264-227

    sX = 170
    sY = 205
     
    imgRGB[sX:sX+dx,sY:sY+dy] = rot_eye

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()


if __name__ =='__main__':
    # readwritepixel()
    readwritepixelRegion()