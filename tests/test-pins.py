"""
tests pin 17, 18, 27, 22, 23
you might want to connect an LED to these pins for visual feedback, with a resistor of course. I used 390ohm
"""
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print(sys.argv)

#setup all the pins
pins = [17, 18, 27, 22, 23]
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)

def on(pin):
	GPIO.output(pin, GPIO.HIGH)
def off(pin):
	GPIO.output(pin, GPIO.LOW)

for pin in pins:
	print("NOW AT PIN", pin)
	s = input("press enter to turn pin on")
	on(pin)
	time.sleep(1.5)
	off(pin)
	time.sleep(1.5)
	print("Test passed for pin:", pin)

print("EXITING")
GPIO.cleanup()