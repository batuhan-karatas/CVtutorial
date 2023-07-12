import cv2 as cv

#capture = cv.VideoCapture("Resources/Videos/dog.mp4")
capture = cv.VideoCapture(0)

#resolution of live video 3--width,4--height
capture.set(3,5000)
capture.set(4,5000)

def reScale(frame,scale = 0.75):
    # work for images, videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimentions =(width,height)

    return cv.resize(frame, dimentions, interpolation= cv.INTER_AREA)

while True:
   isTrue, frame = capture.read()

   #rescaledframe = reScale(frame)
   cv.imshow("Video", frame)

   #cv.imshow("ScaledVideo", rescaledframe)

   if cv.waitKey(20) & 0xFF == ord("d"):
       break
capture.release()
cv.destroyAllWindows()
image = cv.imread("Resources/Photos/cat.jpg")

resizedimage = reScale(image)

cv.imshow("image",image)
cv.imshow("resizedimage",resizedimage)

cv.waitKey(0)