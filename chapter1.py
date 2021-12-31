import cv2
print("Package imported successfully")

# Reading Images
img = cv2.imread('./resources/gorilla.jpg')
cv2.imshow("Output",img) # first arg - name of the window, second arg = name of img (variable)

#by above line the image window will appear but will not stop therefore use cv2.waitKey(0) - 0 means wait for inf time, 1 means - 1 milisecond
cv2.waitKey(0)

