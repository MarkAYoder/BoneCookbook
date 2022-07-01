#!/usr/bin/env python
# ////////////////////////////////////////
# //	i2ctmp101.py
# //      Read at TMP101 sensor on i2c bus 2, address 0x49
# //	Wiring:	Attach to i2c as shown in text.
# //	Setup:	pip install smbus
# //	See:	
# ////////////////////////////////////////
import smbus
import time

ms = 1000               # Read time in ms
bus = smbus.SMBus(2)    # Using i2c bus 2
addr = 0x49             # TMP101 is at address 0x49

while True:
    data = bus.read_byte_data(addr, 0)
    print("temp (C) = " + str(data))
    time.sleep(ms/1000)
