import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo, GPIO.OUT)

p= GPIO.PWM(servo, 50) #50hz frequency = 20 ms

p.start(2.5) #starting duty at 0 degree

try:
	while True:
		for x in range(11):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.03)
			print(x)

		for x in range(9,0,-1):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.03)
			print (x)

except KeyboardInterrupt:
	GPIO.cleanup()
