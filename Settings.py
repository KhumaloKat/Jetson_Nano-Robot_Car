"""
----Give Permission to port for Arduino
sudo chmod 666 /dev/ttyACM0

-----Change the mode to 5W for using USB power
sudo nvpmodel -m1
sudo nvpmodel -q

----Camset
flip =  0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264,
 height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+'
  ! video/x-raw, width='+str(frameWidth)+', height='+str(frameHeight)+',
   format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap = cv2.VideoCapture(camSet)

gst-launch-1.0 nvarguscamerasrc sensor_id=1 ! \
   'video/x-raw(memory:NVMM),width=1270, height=720, framerate=30/1' ! \
   nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=540' ! \
   nvvidconv ! nvegltransform ! nveglglessink -e
"""