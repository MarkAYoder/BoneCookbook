#!/usr/bin/env python
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
import os
from flask import Flask, render_template
app = Flask(__name__)

pin = '30' #  P9_11 is gpio 30
GPIOPATH="/sys/class/gpio"
buttonSts = 0

# Make sure pin is exported
if (not os.path.exists(GPIOPATH+"/gpio"+pin)):
    f = open(GPIOPATH+"/export", "w")
    f.write(pin)
    f.close()

# Make it an input pin
f = open(GPIOPATH+"/gpio"+pin+"/direction", "w")
f.write("in")
f.close()

@app.route("/")
def index():
	# Read Button Status
	f = open(GPIOPATH+"/gpio"+pin+"/value", "r")
	buttonSts = f.read()[:-1]
	f.close()

	# buttonSts = GPIO.input(button)
	templateData = {
      'title' : 'GPIO input Status!',
      'button'  : buttonSts,
      }
	return render_template('index2.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)