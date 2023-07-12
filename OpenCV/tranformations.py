import cv2 as cv
import numpy as np
def translate(image, x, y):
    trans = np.float32([[1,0,x],[0,1,y]])
    print(trans)
    dimentions = (image.shape[1],image.shape[0])

    return cv.warpAffine(image,trans,dimentions)

def rotate (image, angle, rotPoint = None):
    (height, width) = image.shape[:2]


    if rotPoint == None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    print(rotMat)
    dimentions = (width,height)
    return cv.warpAffine(image,rotMat,dimentions)
image = cv.imread("Resources/Photos/group 1.jpg")

cv.imshow("Image",image)

transimage = translate(image,100,100)
cv.imshow("transimage",transimage)

#rotation
rotimage = rotate(image,45)
cv.imshow("rotimage",rotimage)

#resizeing
resized = cv.resize(image,(600,600),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resized)

#flipping
flip = cv.flip(image,0)
cv.imshow("flip",flip)

#cropping

cropedimage = image[100:200,400:500]
cv.imshow("cropted",cropedimage)
cv.waitKey(0)