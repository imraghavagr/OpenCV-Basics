import cv2
import numpy as np

#Some basic functions

img = cv2.imread('./resources/sammy.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow("GrayImg",imgGray)

#blur image using Gaussian Blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # second arg is kernal number [must be oddXodd] eg 3X3, 7X7.. third arg is sigmaX
#cv2.imshow("BlurImage",imgBlur)

# Edge Detector[ Canny edge detector ]
imgCanny = cv2.Canny(img,200,100) #img, threshold values
cv2.imshow("CannyImage",imgCanny)

#
cv2.waitKey(0)


