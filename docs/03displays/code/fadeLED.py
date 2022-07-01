#!/usr/bin/env python
# ////////////////////////////////////////
# //	fadeLED.py
# //	Blinks the P9_14 pin
# //	Wiring:
# //	Setup:  config-pin P9_14 pwm
# //          cd /sys/class/pwm/pwmchip5
# //          echo 0 > export
# //          cd pwm0
# //          chgrp gpio *
# //          chmod g+w *
# //	See:
# ////////////////////////////////////////
import time
ms = 20;   # Fade time in ms

pwmPeriod = 1000000    # Period in ns
pwmchip = '5'  # pwm chip to use
pwm = '0'      # pwm to use
PWMPATH='/sys/class/pwm/pwmchip'+pwmchip
step = 0.02    # Step size
min = 0.02     # dimmest value
max = 1        # brightest value
brightness = min # Current brightness


# f = open(PWMPATH+'/export')   # Export the pwm channel
# f.write(pwm)
# f.close()

# Set the period in ns, first 0 duty_cycle, 
f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
f.write('0')
f.close()

f = open(PWMPATH+'/pwm'+pwm+'/period', 'w')
f.write(str(pwmPeriod))
f.close()

f = open(PWMPATH+'/pwm'+pwm+'/enable', 'w')
f.write('1')
f.close()

f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
while True:
    f.seek(0)
    f.write(str(round(pwmPeriod*brightness)))
    brightness = brightness + step
    if(brightness >= max or brightness <= min):
        step = -1 * step
    time.sleep(ms/1000)
