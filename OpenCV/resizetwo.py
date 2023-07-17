import cv2 as cv

img= cv.imread("Resources/Photos/disaster.jpg")

#cv.INTER_AREA for shirinking
resized_area = cv.resize(img,(1000,500),interpolation=cv.INTER_AREA)
cv.imshow("Area",resized_area)

#cv.INTER_CUBIC slow but efficient
resized_cubic = cv.resize(img,(1000,500),interpolation=cv.INTER_CUBIC)
cv.imshow("cubic",resized_cubic)

#default
resized_linear = cv.resize(img,(1000,500),interpolation=cv.INTER_LINEAR)
cv.imshow("Linear",resized_linear)

cv.erode()
cv.waitKey(0)
cv.destroyAllWindows()