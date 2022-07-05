#!/usr/bin/env python
# // This uses the eQEP hardware to read a rotary encoder
# // and position a servo motor
# // bone$ config-pin P8_11 qep
# // bone$ config-pin P8_12 qep
# //          cd /sys/bus/counter/devices/counter2/count0
# //          sudo chgrp gpio *
# //          sudo chmod g+w *
import time
import signal
import sys

# Set up encoder
eQEP = '2'
COUNTERPATH = '/sys/bus/counter/devices/counter'+eQEP+'/count0'
maxCount = '180'

ms = 100 	# Time between samples in ms

# Set the eEQP maximum count
fQEP = open(COUNTERPATH+'/ceiling', 'w')
fQEP.write(maxCount)
fQEP.close()

# Enable
fQEP = open(COUNTERPATH+'/enable', 'w')
fQEP.write('1')
fQEP.close()

fQEP = open(COUNTERPATH+'/count', 'r')

# Set up servo
pwmPeriod = '20000000'    # Period in ns, (20 ms)
pwmchip = '5'  # pwm chip to use
pwm = '1'      # pwm to use
PWMPATH='/sys/class/pwm/pwmchip'+pwmchip
min  = 0.8 # Smallest angle (in ms)
max  = 2.4 # Largest angle (in ms)
ms   = 250 # How often to change position, in ms
pos  = 1.5 # Current position, about middle ms)
step = 0.1 # Step size to next position

def signal_handler(sig, frame):
    print('Got SIGINT, turning motor off')
    f = open(PWMPATH+'/pwm'+pwm+'/enable', 'w')
    f.write('0')
    f.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

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

print('Hit ^C to stop')

olddata = -1
while True:
	fQEP.seek(0)
	data = fQEP.read()[:-1]
	# Print only if data changes
	if data != olddata:
		olddata = data
		print("data = " + data)
		# # map 0-180  to min-max
		duty_cycle = int(data)*(max-min)/180.0 + min
		duty_cycle = str(int(duty_cycle*1000000))	# Convert from ms to ns
		print('duty_cycle = ' + duty_cycle)
		f = open(PWMPATH+'/pwm'+pwm+'/duty_cycle', 'w')
		f.write(duty_cycle)
		f.close()
	time.sleep(ms/1000)

# Black OR Pocket
# eQEP0:	P9.27 and P9.42 OR P1_33 and P2_34
# eQEP1:	P9.33 and P9.35
# eQEP2:	P8.11 and P8.12 OR P2_24 and P2_33

# AI
# eQEP1:	P8.33 and P8.35
# eQEP2:	P8.11 and P8.12 or P9.19 and P9.41
# eQEP3:	P8.24 abd P8.25 or P9.27 and P9.42