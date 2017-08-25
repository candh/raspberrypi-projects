from flask import Flask
from flask import render_template, url_for
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

app = Flask(__name__)
socketio = SocketIO(app)

pins = { 'relay1': 17, 'relay2': 18 }

@app.route('/')
def hello(name=None):
	print("Initializing")
	for pin in pins.values():
		GPIO.setup(pin, GPIO.OUT)
		# BECAUSE THE RELAY TURNS ON WHEN THE GPIO PIN is set to LOW so we 
		# have to init it to HIGH 
		GPIO.output(pin, GPIO.HIGH)

	return render_template('index.html', pins=pins)


@socketio.on('onPin')
def handle_on(pin):
	print('turn pin on: ' + pin)
	GPIO.output(int(pin), GPIO.LOW)


@socketio.on('offPin')
def handle_off(pin):
	print('turn pin off: ' + pin)
	GPIO.output(int(pin), GPIO.HIGH)


if __name__ == '__main__':
	socketio.run(app)