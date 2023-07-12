import cv2 as cv
image = cv.imread("Resources/Photos/cat_large.jpg")
cv.imshow("Cat",image)

cv.waitKey(0)

#capture = cv.VideoCapture("Resources/Videos/dog.mp4")
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()