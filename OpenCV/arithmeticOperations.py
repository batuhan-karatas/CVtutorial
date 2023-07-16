import sys

import cv2 as cv
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
image1 = cv.imread("Resources/Photos/disaster.jpg")
image2 = cv.imread("Resources/Photos/space.jpg")

image1 = cv.resize(image1,(10,10), interpolation=cv.INTER_AREA)
image2 = cv.resize(image2,(10,10), interpolation=cv.INTER_AREA)
weightedSum = cv.addWeighted(image1,0.5,image2,0.5,1)

cv.imshow("image1",image1)
cv.imshow("image2",image2)
cv.imshow("Weightedsum",weightedSum)
subimg = cv.subtract(image1,image2)

#perfect
cv.imshow("sub",subimg)

print("----------Image1------------\n",image1,"\n----------Image2------------\n",image2,"\n----------Sub------------\n",subimg)

cv.waitKey(0)
cv.destroyAllWindows()
