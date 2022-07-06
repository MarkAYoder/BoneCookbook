#!/usr/bin/env python
# ////////////////////////////////////////
# //	dcMotor.js
# //	This is an example of driving a DC motor
# //	Wiring:
# //	Setup:  config-pin P9_16 pwm
# //	See:
# ////////////////////////////////////////
import time
import signal
import sys

def signal_handler(sig, frame):
    print('Got SIGINT, turning motor off')
    f = open(PWMPATH+'/enable', 'w')
    f.write('0')
    f.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

pwmPeriod = '1000000'    # Period in ns
pwm     = '1'  # pwm to use
channel = 'b'  # channel to use
PWMPATH='/dev/bone/pwm/'+pwm+'/'+channel

low = 0.05     # Slowest speed (duty cycle)
hi  = 1        # Fastest (always on)
ms = 100       # How often to change speed, in ms
speed = 0.5    # Current speed
step = 0.05    # Change in speed

f = open(PWMPATH+'/duty_cycle', 'w')
f.write('0')
f.close()
f = open(PWMPATH+'/period', 'w')
f.write(pwmPeriod)
f.close()
f = open(PWMPATH+'/enable', 'w')
f.write('1')
f.close()

f = open(PWMPATH+'/duty_cycle', 'w')
while True:
    speed += step
    if(speed > hi or speed < low):
        step *= -1
    duty_cycle = str(round(speed*1000000))    # Convert ms to ns
    f.seek(0)
    f.write(duty_cycle)
    time.sleep(ms/1000)
