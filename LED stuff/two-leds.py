"""
requires 2 LED and uses pin 17, 18, flickers them

"""
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
speed = 0.3

def on(pin):
	GPIO.output(pin, GPIO.HIGH)
def off(pin):
	GPIO.output(pin, GPIO.LOW)

try:
	while True:
		on(17)
		time.sleep(speed)
		off(17)
		time.sleep(speed)
		on(18)
		time.sleep(speed)
		off(18)
		time.sleep(speed)
except:
	GPIO.cleanup()
	print("EXITING")
