import sys

import cv2 as cv
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
img = cv.imread("Resources/Photos/cats.jpg")
img = cv.resize(img,(10,10))
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(img)
cv.imshow("Cats",img)

blank = np.zeros(img.shape, dtype = "uint8")
cv.imshow("blank",blank)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

canny = cv.Canny(img, 125,175)
cv.imshow("canny",canny)

ret, thresh = cv.threshold(img,15,2054,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
print(hierarchies)
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("draw contour from tresh",blank)

cv.waitKey(0)
cv.destroyAllWindows()