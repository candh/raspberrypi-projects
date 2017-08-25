"""
requires one LED and uses pin 18
note that i just made it like this, i am not sure if this is how morse code works. I didn't look it up, lol

"""
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

morse = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

def on():
		GPIO.output(18, GPIO.HIGH)
def off():
		GPIO.output(18, GPIO.LOW)
def indicator():
	print("its gonna over now")
	for i in range(3):
		on()
		time.sleep(0.2)
		off()
		time.sleep(0.2)
for c in morse:
	if c == ".":
		print("dot")
		on()
		time.sleep(1)
		off()
		time.sleep(1)
	elif c == "-":
		print("dash")
		on()
		time.sleep(2)
		off()
		time.sleep(2)
	else:
		print("space or / ")
		off()
		time.sleep(1)
indicator()
