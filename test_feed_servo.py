import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
servo= GPIO.PWM(11,50)
servo.start(7)
for i in range(0,90):
	x=1./18.*(i)+2
	servo.ChangeDutyCycle(x)
	time.sleep(0.25)
for i in range(90,0,-1):
	x=1/18.*i+2
	servo.ChangeDutyCycle(x)
	time.sleep(0.25)
servo.stop()
GPIO.cleanup()
