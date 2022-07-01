#!/usr/bin/env python
# ////////////////////////////////////////
# //	w1.js
# //      Read a Dallas 1-wire device on P9_12
# //	Wiring:	Attach gnd and 3.3V and data to P9_12
# //	Setup:	Edit /boot/uEnv.txt to include:
# //              uboot_overlay_addr4=BB-W1-P9.12-00A0.dtbo
# //	See:	
# ////////////////////////////////////////
import time

ms = 500   # Read time in ms
#  Do ls /sys/bus/w1/devices and find the address of your device
addr = '28-00000d459c2c' # Must be changed for your device.
W1PATH ='/sys/bus/w1/devices/' + addr

f = open(W1PATH+'/temperature')

while True:
    f.seek(0)
    data = f.read()[:-1]
    print("temp (C) = " + str(int(data)/1000))
    time.sleep(ms/1000)
