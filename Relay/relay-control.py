"""
TURNS THE SPECIFIED GPIO LOW WHEN THE SCRIPT IS RAN. this is for relays because when the pin is OFF, the relay turns ON
and when the GPIO is ON or HIGH, the relay is off. Learned this the hard way.
"""
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin = int(sys.argv[1])

GPIO.output(pin, GPIO.HIGH)

def on(pin):
	GPIO.output(pin, GPIO.LOW)

def off(pin):
	GPIO.output(pin, GPIO.HIGH)


try:
	print(pin, "is on!")
	on(pin)
	time.sleep(3)
	off(pin)
	GPIO.cleanup()
except:
	off(pin)
	GPIO.cleanup()
	print("Exiting!")
