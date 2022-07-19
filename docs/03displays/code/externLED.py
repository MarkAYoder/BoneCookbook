#!/usr/bin/env python
# ////////////////////////////////////////
# //	externalLED.py
# //	Blinks an external LED wired to P9_14.
# //	Wiring: P9_14 connects to the plus lead of an LED.  The negative lead of the
#			LED goes to a 220 Ohm resistor.  The other lead of the resistor goes
#			to ground.
# //	Setup:
# //	See:
# ////////////////////////////////////////
import time
import os

ms = 250        # Time to blink in ms
# Look up P9.14 using gpioinfo | grep -e chip -e P9.14.  chip 1, line 18 maps to 50
pin = '50'

GPIOPATH='/sys/class/gpio/'
# Make sure pin is exported
if (not os.path.exists(GPIOPATH+"gpio"+pin)):
    f = open(GPIOPATH+"export", "w")
    f.write(pin)
    f.close()

# Make it an output pin
f = open(GPIOPATH+"gpio"+pin+"/direction", "w")
f.write("out")
f.close()
 
f = open(GPIOPATH+"gpio"+pin+"/value", "w")
# Blink
while True:
    f.seek(0)
    f.write("1")
    time.sleep(ms/1000)

    f.seek(0)
    f.write("0")
    time.sleep(ms/1000)
f.close()
