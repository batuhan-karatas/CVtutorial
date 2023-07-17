# Python program to illustrate
# corner detection with
# Shi-Tomasi Detection Method

# organizing imports
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# path to input image specified and
# image is loaded with imread command
img = cv2.imread('Resources/Photos/disaster.jpg')

# convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi corner detection function
# We are detecting only 100 best corners here
# You can change the number to get desired result.
corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)

# convert corners values to integer
# So that we will be able to draw circles on them
corners = np.intp(corners)
print(corners)
# draw red color circles on all corners
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)



cv2.imshow("image",img)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
