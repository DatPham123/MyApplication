import RPi.GPIO as GPIO
import io
import time
from picamera import PiCamera
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

stream = io.BytesIO()
camera = PiCamera()
time2 = datetime.now()

i=0

def LiveStream():
	#camera.start_preview()
	#GPIO.output(3,1)
	print ("It did something")

while True:
	i+=1
        state = GPIO.input(26)
        if state==0:	#low
                print "No Detection"
		GPIO.output(3,0)	#LED
                time.sleep(1)
        elif state==1: #high 
                print "Motion Detected"
		GPIO.output(3,1)	#LED
		#camera.capture('/home/pi/IoT/pics/image{0:04}.jpg'.format(time2.second+i))
		#camera.capture('/home/pi/IoT/pics/image{%02d--%02d:%02d:%02d}.jpg' % (time2.day, time2.hour, time2.minute, time2.second+i-1))
                camera.capture('/home/pi/Desktop/IoT/pics/image{%04d-%02d-%02d--%02d:%02d:%02d}.jpg' % (time2.year, time2.month, time2.day, time2.hour, time2.minute, time2.second+i-1))
                #camera.resolution = (640,480)
		#camera.start_recording(stream, format='h264', quality=23)
		#camera.start_recording('my_video.h264')
		#camera.wait_recording(10)
		#camera.stop_recording()
		#stream.read()
		time.sleep(1)
