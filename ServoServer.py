import Socket_Servo
from socket import *
from time import ctime
import RPi.GPIO as GPIO
Socket_Servo.Setup()

ctrCmd = ['U','D',"F"]

HOST = ''
PORT = 3000
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.listen(5)

while True:
	print ("Waiting for connection")
	tcpCliSock,addr = tcpSock.accept()
	print ('connected from: ', addr)
	try:
		while True:
			stringdata = ''
			data = tcpCliSock.recv(BUFSIZE)
			data = str(data.decode('utf-8'))
			print("data is:", data)
			if not data:
                                break;
			if data == ctrCmd[0]:
				print("0: ", data)
				Socket_Servo.ServoUp()
			print ("Up: ", Socket_Servo.x)
			if data == ctrCmd[1]:
				print("1: ", data)
				Socket_Servo.ServoDown()
			print ("Down: ", Socket_Servo.x)
			if data == ctrCmd[2]:
				print("2: ", data)
				Socket_Servo.ServoFeed()
			print ("Feed: ", Socket_Servo.x)
	except KeyboardInterrupt:
			GPIO.cleanup()
			Socket_Servo.close()
             	#print 'error/exception'

tcpSock.close()
