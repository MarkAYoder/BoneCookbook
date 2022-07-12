#!/usr/bin/env python
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
# import Adafruit_BBIO.GPIO as GPIO
import os
from flask import Flask, render_template, request
app = Flask(__name__)
#define LED GPIO
ledRed = "P9_14"
pin = '50' #  P9_14 is gpio 50
GPIOPATH="/sys/class/gpio"

#initialize GPIO status variable
ledRedSts = 0
# Make sure pin is exported
if (not os.path.exists(GPIOPATH+"/gpio"+pin)):
    f = open(GPIOPATH+"/export", "w")
    f.write(pin)
    f.close()
# Define led pin as output
f = open(GPIOPATH+"/gpio"+pin+"/direction", "w")
f.write("out")
f.close()
# turn led OFF 
f = open(GPIOPATH+"/gpio"+pin+"/value", "w")
f.write("0")
f.close()

@app.route("/")
def index():
	# Read Sensors Status
	f = open(GPIOPATH+"/gpio"+pin+"/value", "r")
	ledRedSts = f.read()
	f.close()
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : ledRedSts,
        }
	return render_template('index3.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
	f = open(GPIOPATH+"/gpio"+pin+"/value", "w")
	if action == "on":
		f.write("1")
	if action == "off":
		f.write("0")
	f.close()
		     
	f = open(GPIOPATH+"/gpio"+pin+"/value", "r")
	ledRedSts = f.read()
	f.close()

	templateData = {
              'ledRed'  : ledRedSts,
	}
	return render_template('index3.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)