import cv2 as cv
import matplotlib.pyplot as plt
image = cv.imread("Resources/Photos/cat_large.jpg")
plt.imshow(image)
plt.waitforbuttonpress()
plt.close("all")
cv.imshow("Cat",image)
shape = image.shape
print(shape)
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