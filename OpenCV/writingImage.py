import cv2 as cv

import os

image = cv.imread("Resources/Photos/cat.jpg")

cv.imshow("image",image)


newimage = cv.rectangle(image,(150,200),(200,220),(125,26,95),-1)

cv.imshow("newimage",newimage)

os.chdir("Resources/Photos")
cv.imwrite("newimage2.jpg",newimage)

cv.waitKey(0)

cv.destroyAllWindows()

