#!/usr/bin/env python
# ////////////////////////////////////////
# //	i2cTemp.py
# //      Read a TMP101 sensor on i2c bus 2, address 0x49
# //	Wiring:	Attach to i2c as shown in text.
# //	Setup:	echo tmp101 0x49 > /sys/class/i2c-adapter/i2c-2/new_device
# //	See:	
# ////////////////////////////////////////
import time

ms = 1000   # Read time in ms
bus = '2'
addr = '49'
I2CPATH='/sys/class/i2c-adapter/i2c-'+bus+'/'+bus+'-00'+addr+'/hwmon/hwmon0';

f = open(I2CPATH+"/temp1_input", "r")

while True:
    f.seek(0)
    data = f.read()[:-1]    # returns mili-degrees C
    print("data (C) = " + str(int(data)/1000))
    time.sleep(ms/1000)