import os 
import time
from TwitterAPI import TwitterAPI
from gpiozero import MotionSensor
#importing required libraries

pir = MotionSensor(4)
#pir sensor connecter to gpio4
CONSUMER_KEY = 	''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
#giving required details
img="/home/pi/cam/img.jpg"

#creating a function to take a pic
def mypic():
    #command to take a pic
    cmd= "fswebcam -F 5 --fps 20 -r \"1200x800\" "+img
    os.system(cmd)
    print("pic taken")

#creating a function to tweet 
def mytweet():
    #open file 
    file = open(img, 'rb')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
    print(r.status_code)

#creating a while loop
while True: 
    if pir.motion_detected:
        mypic()
        mytweet()
