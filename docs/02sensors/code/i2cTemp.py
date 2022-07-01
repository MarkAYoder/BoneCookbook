#!/usr/bin/env python
# ////////////////////////////////////////
# //	i2cTemp.js
# //      Read at TMP101 sensor on i2c bus 2, address 0x49
# //	Wiring:	Attach to i2c as shown in text.
# //	Setup:	
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
    data = f.read()[:-1]
    print("data = " + str(int(data)/1000))
    time.sleep(ms/1000)