import cv2
import cv2 as cv
import numpy as np

image1 = np.zeros((600,600,3),np.uint8)
image1[0:300] =(255,255,255)


image2 = np.zeros((600,600,3),np.uint8)

image2 = cv.circle(image2,(300,300),90,(255,255,255),-1)
cv.imshow("image1",image1)
cv.imshow("image2",image2)

andopt = cv2.bitwise_and(image2,image1,mask=None)
cv.imshow("and",andopt)

oropt = cv.bitwise_or(image2,image1,mask=None)
cv.imshow("or",oropt)

xoropt = cv.bitwise_xor(image2,image1,mask=None)
cv.imshow("xor",xoropt)

notopt = cv.bitwise_not(image2,image1,mask=None)
cv.imshow("not",notopt)


cv.waitKey(0)
cv.destroyAllWindows()