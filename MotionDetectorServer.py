import RPi.GPIO as GPIO
import io
import time
import pyimgur

#from StreamingServer import camera
from picamera import PiCamera
from datetime import datetime
from twilio.rest import Client

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)		#Motion Censor
GPIO.setup(3, GPIO.OUT)		#LED

GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


stream = io.BytesIO()
camera = PiCamera()
time2 = datetime.now()

#Twilio info
account_sid ='ACd09ada0263787553419e339016fcb5b7'
auth_token = 'a467c0060f2aff0a30dcca5acbfc0d77'
client = Client(account_sid, auth_token)

##pyimgur info
CLIENT_ID = '76ebb18bdb6c6c9'
PATH = 'UCO.jpg'
URL = 'imgur.com'
im = pyimgur.Imgur(CLIENT_ID)

i=0
FOOD = False
while True:
	i+=1

	state = GPIO.input(26)

	#Weight
	print(GPIO.input(16))
	if GPIO.input(16) == 0:

		if FOOD == True:
               		 message = client.messages \
                        	  .create(
                             		 body = "Load up your Bird Feeder App and refill the food container!",
                             		 from_ =+14052941725,
					 to = +14058157798
                             		 )
                	 print(message.sid)
		 	 FOOD = False
	elif GPIO.input(16) == 1:
		FOOD = True
	#motion
	if state==0:	#low
                print ("No Detection")

		GPIO.output(3,0)

		time.sleep(1)
        elif state==1: #high 
                print ("Motion Detected")
		GPIO.output(3,1)	#LED
                PATH = '/home/pi/Desktop/IoT/pics/image{%04d-%02d-%02d--%02d:%02d:%02d}.jpg' % (time2.year, time2.month, time2.day, time2.hour, time2.minute, time2.second+i-1)
                camera.capture(PATH)
                ##Make not send message every time TO DO
                uploaded_image = im.upload_image(PATH, title = 'Bird feeder upload')
                URL = uploaded_image.link
                message = client.messages \
                          .create(
                              body = "Motion Detected! Load up your Bird feeder app to start viewing!",
                              from_ =+14052941725,
                              media_url = URL,
                              to = +14058157798
                              )
                print(message.sid)
		time.sleep(1)
