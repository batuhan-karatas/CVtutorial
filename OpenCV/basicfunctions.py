import cv2 as cv

image = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("Image",image)

#convert grayscale
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("GrayImage",gray)

#blur
blur = cv.GaussianBlur(image,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)


#edge cascade
canny = cv.Canny(image,125,175)
cv.imshow("cannyedges",canny)

#dialatee

dialet = cv.dilate(canny,(3,3), iterations=1)
cv.imshow("dialet",dialet)

#erode
erode = cv.erode(image,(3,3),iterations=5)
cv.imshow("erode",erode)

#resize
resize = cv.resize(image,(500,500), interpolation=cv.INTER_LINEAR)
cv.imshow("resized",resize)

#cropping

cropped = image[50:200,200:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)
