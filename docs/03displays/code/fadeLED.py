#!/usr/bin/env python
# ////////////////////////////////////////
# //	fadeLED.py
# //	Blinks the P9_14 pin
# //	Wiring:
# //	Setup:  config-pin P9_14 pwm
# //	See:
# ////////////////////////////////////////
import time
ms = 20;   # Fade time in ms

pwmPeriod = 1000000    # Period in ns
pwm     = '1'  # pwm to use
channel = 'a'  # channel to use
PWMPATH='/dev/bone/pwm/'+pwm+'/'+channel
step = 0.02    # Step size
min = 0.02     # dimmest value
max = 1        # brightest value
brightness = min # Current brightness

f = open(PWMPATH+'/period', 'w')
f.write(str(pwmPeriod))
f.close()

f = open(PWMPATH+'/enable', 'w')
f.write('1')
f.close()

f = open(PWMPATH+'/duty_cycle', 'w')
while True:
    f.seek(0)
    f.write(str(round(pwmPeriod*brightness)))
    brightness  += step
    if(brightness >= max or brightness <= min):
        step = -1 * step
    time.sleep(ms/1000)

# | Pin   | pwm | channel
# | P9_31 | 0   | a
# | P9_29 | 0   | b
# | P9_14 | 1   | a
# | P9_16 | 1   | b
# | P8_19 | 2   | a
# | P8_13 | 2   | b