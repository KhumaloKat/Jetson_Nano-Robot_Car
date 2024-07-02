"""
Give Permission to port for Arduino
sudo chmod 666 /dev/ttyACM0

Change the mode to 5W for using USB power
sudo nvpmodel -m1
sudo nvpmodel -q

"""
import cv2
import time
import SerialModule as sm
ser = sm.initConnection('/dev/ttyACM0', 9600)

frameWidth = 640
frameHeight= 480


cap = cv2.VideoCapture(0)
ca
while True:
    _, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    key = cv2.waitKey(1)
    if key == ord('w'):sm.sendData(ser,[50,0],4)
    elif key == ord('s'):sm.sendData(ser,[-50,0],4)
    elif key == ord('a'):sm.sendData(ser,[50,15],4)
    elif key == ord('d'):sm.sendData(ser,[50,-15],4)
    elif key == ord('q'):break
    
    else: sm.sendData(ser,[0,0],4)