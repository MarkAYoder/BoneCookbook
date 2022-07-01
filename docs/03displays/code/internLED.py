#!/usr/bin/env python
# //////////////////////////////////////
# 	internalLED.py
# 	Blinks A USR LED.
# 	Wiring:
# 	Setup:
# 	See:
# //////////////////////////////////////
import time

ms = 250      # Blink time in ms
LED = 'usr0'; # LED to blink
LEDPATH = '/sys/class/leds/beaglebone:green:'+LED+'/brightness'

state = '1'    # Initial state

f = open(LEDPATH, "w")

while True:
    f.seek(0)
    f.write(state)
    if (state == '1'):
        state = '0'
    else:
        state = '1'
    time.sleep(ms/1000)