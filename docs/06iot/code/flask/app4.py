#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
import os
# import Adafruit_BBIO.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIOPATH="/sys/class/gpio"
#define sensors GPIOs
button = "30"  # "P9_11"
#define actuators GPIOs
ledRed = "50"  # "P9_14"

# Make sure pin is exported
if (not os.path.exists(GPIOPATH+"/gpio"+button)):
    f = open(GPIOPATH+"/export", "w")
    f.write(pin)
    f.close()
if (not os.path.exists(GPIOPATH+"/gpio"+ledRed)):
    f = open(GPIOPATH+"/export", "w")
    f.write(pin)
    f.close()
#initialize GPIO status variables
buttonSts = 0
ledRedSts = 0
# Define button and PIR sensor pins as an input
# GPIO.setup(button, GPIO.IN)  
f = open(GPIOPATH+"/gpio"+button+"/direction", "w")
f.write("in")
f.close() 
# Define led pins as output
# GPIO.setup(ledRed, GPIO.OUT) 
f = open(GPIOPATH+"/gpio"+ledRed+"/direction", "w")
f.write("out")
f.close()  
# turn leds OFF 
# GPIO.output(ledRed, GPIO.LOW)
f = open(GPIOPATH+"/gpio"+ledRed+"/value", "w")
f.write("0")
f.close()

@app.route("/")
def index():
	# Read GPIO Status
	# buttonSts = GPIO.input(button)
	f = open(GPIOPATH+"/gpio"+button+"/value", "r")
	buttonSts = f.read()
	f.close()
	# ledRedSts = GPIO.input(ledRed)
	f = open(GPIOPATH+"/gpio"+ledRed+"/value", "r")
	ledRedSts = f.read()
	f.close()

	templateData = {
      		'button'  : buttonSts,
      		'ledRed'  : ledRedSts,
      	}
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed

	f = open(GPIOPATH+"/gpio"+ledRed+"/value", "w")
	if action == "on":
		# GPIO.output(actuator, GPIO.HIGH)
		f.write("1")
	if action == "off":
		# GPIO.output(actuator, GPIO.LOW)
		f.write("0")
	f.close()
		     
	# buttonSts = GPIO.input(button)
	# ledRedSts = GPIO.input(ledRed)
	# buttonSts = GPIO.input(button)
	f = open(GPIOPATH+"/gpio"+button+"/value", "r")
	buttonSts = f.read()
	f.close()
	# ledRedSts = GPIO.input(ledRed)
	f = open(GPIOPATH+"/gpio"+ledRed+"/value", "r")
	ledRedSts = f.read()
	print("ledRedSts: " + ledRedSts)
	f.close()

	templateData = {
	 	'button'  : buttonSts,
  		'ledRed'  : ledRedSts,
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)