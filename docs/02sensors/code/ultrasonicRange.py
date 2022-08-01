#!/usr/bin/env python
# //////////////////////////////////////
# //	ultrasonicRange.js
# // 	Reads the analog value of the sensor.
# //////////////////////////////////////
import time
ms = 250;  # Time in milliseconds

pin = "0"        # sensor, A0, P9_39

IIOPATH='/sys/bus/iio/devices/iio:device0/in_voltage'+pin+'_raw'

print('Hit ^C to stop');

f = open(IIOPATH, "r")
while True:
    f.seek(0)
    data = f.read()[:-1]
    print('data= ' + data)
    time.sleep(ms/1000)

# // Bone  | Pocket | AIN
# // ----- | ------ | --- 
# // P9_39 | P1_19  | 0
# // P9_40 | P1_21  | 1
# // P9_37 | P1_23  | 2
# // P9_38 | P1_25  | 3
# // P9_33 | P1_27  | 4
# // P9_36 | P2_35  | 5
# // P9_35 | P1_02  | 6
