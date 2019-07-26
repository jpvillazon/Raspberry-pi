import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)

i=0
try:
	while True:
		if GPIO.input(23):
			i=i+1
			print i
			time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()


