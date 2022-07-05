#!/usr/bin/env python
# ////////////////////////////////////////
# //	dcMotor.js
# //	This is an example of driving a DC motor
# //	Wiring:
# //	Setup:  config-pin P9_16 pwm
# //          cd /sys/class/pwm/pwmchip5
# //          echo 1 > export
# //          cd pwm1
# //          chgrp gpio *
# //          chmod g+w *
# //	See:
# ////////////////////////////////////////
import time
import signal
import sys

def signal_handler(sig, frame):
    print('Got SIGINT, turning motor off')
    f = open(PWMPATH+'/pwm'+pwm+'/enable', 'w')
    f.write('0')
    f.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

pwmPeriod = '1000000'    # Period in ns
pwmchip = '5'  # pwm chip to use
pwm = '1'      # pwm to use
PWMPATH='/sys/class/pwm/pwmchip'+pwmchip

min = 0.05     # Slowest speed (duty cycle)
max = 1        # Fastest (always on)
ms = 100       # How often to change speed, in ms
speed = 0.5    # Current speed
step = 0.05    # Change in speed

# fs.writeFileSync(PWMPATH+'/export', pwm)   # Export the pwm channel
# Set the period in ns, first 0 duty_cycle
# f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
# f.write('0')
# f.close()
f = open(PWMPATH+'/pwm'+pwm+'/period', 'w')
f.write(pwmPeriod)
f.close()
f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
f.write(str(round(int(pwmPeriod)/2)))
f.close()
f = open(PWMPATH+'/pwm'+pwm+'/enable', 'w')
f.write('1')
f.close()

while True:
    speed += step
    if(speed > max or speed < min):
        step *= -1
    duty_cycle = str(round(speed*1000000))    # Convert ms to ns
    f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
    f.write(duty_cycle)
    f.close()
    time.sleep(ms/1000)
