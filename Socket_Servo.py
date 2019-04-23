import RPi.GPIO as GPIO
import time

x= 0

def Setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	global servo
	servo=GPIO.PWM(11, 50)
	servo.start(5)

def ServoUp():
	global x
	x += 2.5
	if x > 12:
		x = 12.5
	servo.ChangeDutyCycle(x)
	time.sleep(1)
def ServoDown():
	global x
	x -= 2.5
	if x <2.5:
		x=2.5
	servo.ChangeDutyCycle(x)
	time.sleep(1)
def ServoFeed():
	servo.ChangeDutyCycle(1)
	time.sleep(4)
	servo.ChangeDutyCycle(5)
	time.sleep(4)
def Close():
	GPIO.cleanup()
	servo.stop()
if __name__ =='__main__':
	Setup()
