import cv2

#Some basic functions

img = cv2.imread('./resources/horse.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImg",imgGray)
cv2.waitKey(0)




