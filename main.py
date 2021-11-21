import paramiko
import cv2
from sys import exit
import time
import os
from contextlib import contextmanager
host = '192.168.137.50'
username = 'pi'
password = 'raspberry'

LED_Count = 500


def LightUp():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    stdin,stdout,stderr=ssh.exec_command("cd Desktop;sudo python3 RaspberryConfig.py")
    ssh.close()



def ImageCapture(SET,LED):
    img_name = "{SET}".format(SET=SET)+"{LED}.png".format(LED=LED)
    cv2.imwrite(img_name, frame)
    print(img_name)

def SetLoop(SET,LED):
        LightUp()
        time.sleep(1)
        ImageCapture(SET,LED)

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")
global img_counter
img_counter = 0
global SET,LED
SET = 1
LED = 0
time.sleep(5)

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    SetLoop(SET,LED)
    LED +=1
    if LED == LED_Count:
        SET +=1
        LED = 0
        if SET == 5:
            break
        cv2.waitKey(0)





    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        ImageCapture(img_counter)
        img_counter +=1
        if img_counter == 50:
            exit()


cam.release()

cv2.destroyAllWindows()