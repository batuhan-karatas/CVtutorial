import cv2 as cv
import numpy as np


image = cv.imread("Resources/Photos/disaster.jpg")

operatedImage = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

operatedImage = np.float32(operatedImage)

dest = cv.cornerHarris(operatedImage,2,5,0.07)
dest = cv.dilate(dest,None)

image[dest > 0.01 * dest.max()] = [0,0,255]

cv.imshow("imagewithborders", image)

cv.waitKey(0)
cv.destroyAllWindows()