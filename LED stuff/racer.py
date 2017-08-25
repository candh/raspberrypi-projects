"""
utilizes PIN 17, 18, 27, 22, 23 and turn them on after one another, kind of like a racer. GIVE IT A SPEED AT RUN TIME
"""
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def on(pin):
	GPIO.output(pin, GPIO.HIGH)
def off(pin):
	GPIO.output(pin, GPIO.LOW)


speed = float(sys.argv[1])

#setup all the pins
pins = [17, 18, 27, 22, 23]

for pin in pins:
	GPIO.setup(pin, GPIO.OUT)

try:
	while True:
		for pin in pins[::-1]:
			print("NOW AT PIN", pin)
			on(pin)
			time.sleep(speed)
			off(pin)
			time.sleep(speed)

except:
		print("EXITING")
		GPIO.cleanup()