import RPi.GPIO as GPIO
import time

from twilio.rest import Client

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Twilio
account_sid ='ACd09ada0263787553419e339016fcb5b7'
auth_token = 'a467c0060f2aff0a30dcca5acbfc0d77'
client = Client(account_sid, auth_token)

FOOD = False
while True:
            #Weight
	time.sleep(3)
        print(GPIO.input(16))
        if GPIO.input(16) == 0:
                if FOOD == True:
                         message = client.messages \
                                  .create(
                                         body = "Load up your Bird Feeder App and refill",
                                         from_ =+14052941725,
                                         to = +14058157798
                                         )
                         print(message.sid)
                         FOOD = False
        elif GPIO.input(16) == 1:
                FOOD = True

GPIO.cleanup()
