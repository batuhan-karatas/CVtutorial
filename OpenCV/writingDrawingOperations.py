import cv2 as cv
import numpy as np

blankimage= np.zeros((600,600,3),np.uint8)

cv.circle(blankimage,(300,300),25,(0,255,0),-1)
cv.putText(blankimage,"batuAI",(100,190),cv.FONT_ITALIC,4,(125,86,36),7,cv.LINE_AA)

cv.line(blankimage,(200,200),(400,400),(0,255,0),7)
cv.imshow("blank",blankimage)



cv.waitKey(0)
cv.destroyAllWindows()