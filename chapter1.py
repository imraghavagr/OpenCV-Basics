from typing import Tuple
import cv2
print("Package imported successfully")

# Reading Images
def readDisplayImage():
    
    img = cv2.imread('./resources/gorilla.jpg')

    cv2.imshow("Output",img) # first arg - name of the window, second arg = name of img (variable)

    #by above line the image window will appear but will not stop therefore use cv2.waitKey(0) - 0 means wait for inf time, 1 means - 1 milisecond
    cv2.waitKey(0)



#Reading videos
def readDisplayVideo():

    # 1 - create a video capture

    cap = cv2.VideoCapture("./resources/hand_move.mp4")

    #display video as sequence of imgs
    while True:
        #reading seq of imgs from cap
        success, img = cap.read() #success is true or false
        cv2.imshow("Video", img)
        #for breaking out of the loop, here loop will break once 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #cap.release()

# Reading from webcam
def startWebcam():

    # 1 - create a video capture

    cap = cv2.VideoCapture(0) #just give id of the camera #0-for default webcam. cap - webcam object
    cap.set(3,640) #specific size, width - id no 3
    cap.set(4,480) #height - id no 4
    #lets change the brightness to make it more clear using capture.setting .. id for brightness is 10
    cap.set(10,100)

    while True:
        #reading seq of imgs from cap
        success, img = cap.read() #success is true or false
        cv2.imshow("Video", img)
        #for breaking out of the loop, here loop will break once 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

startWebcam()