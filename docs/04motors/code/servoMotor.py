#!/usr/bin/env python
# ////////////////////////////////////////
# //	servoMotor.py
# //	Drive a simple servo motor back and forth on P9_16 pin
# //	Wiring:
# //	Setup:  config-pin P9_16 pwm
# //          cd /sys/class/pwm/pwmchip5
# //          echo 1 > export
# //          cd pwm1
# //          chgrp Blinks thegpio *
# //          chmod g+w *
# //	See:
# ////////////////////////////////////////
import time

pwmPeriod = '20000000'    # Period in ns, (20 ms)
pwmchip = '5'  # pwm chip to use
pwm = '1'      # pwm to use
PWMPATH='/sys/class/pwm/pwmchip'+pwmchip
min  = 0.8 # Smallest angle (in ms)
max  = 2.4 # Largest angle (in ms)
ms  = 250  # How often to change position, in ms
pos = 1.5  # Current position, about middle ms)
step = 0.1 # Step size to next position

print('Hit ^C to stop')
# fs.writeFileSync(PWMPATH+'/export', pwm)   # Export the pwm channel
# Set the period in ns, first 0 duty_cycle
f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
f.write('0')
f.close()
f = open(PWMPATH+'/pwm'+pwm+'/period', 'w')
f.write(pwmPeriod)
f.close()
f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
f.write(str(round(int(pwmPeriod)/2)))
f.close()
f = open(PWMPATH+'/pwm'+pwm+'/enable', 'w')
f.write('1')
f.close()

# Sweep from min to max position and back again
while True:
    pos += step    # Take a step
    if(pos > max or pos < min):
        step *= -1
    duty_cycle = str(round(pos*1000000))    # Convert ms to ns
    print('pos = ' + str(pos) + ' duty_cycle = ' + duty_cycle)
    f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
    f.write(duty_cycle)
    f.close()
    time.sleep(ms/1000)

process.on('SIGINT', function() {
    console.log('Got SIGINT, turning motor off')
    clearInterval(timer)             # Stop the timer
    fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/enable', '0')
})

# | Pin   | pwmchip | pwm
# | P9_31 | 3       | 0
# | P9_29 | 3       | 1
# | P9_14 | 5       | 0
# | P9_16 | 5       | 1
# | P8_19 | 7       | 0
# | P8_13 | 7       | 1