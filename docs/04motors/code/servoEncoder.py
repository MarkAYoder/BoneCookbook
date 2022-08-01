#!/usr/bin/env python
# ////////////////////////////////////////
# //	servoEncoder.py
# //	Drive a simple servo motor using rotary encoder viq eQEP 
# //	Wiring: Servo on P9_16, rotary encoder on P8_11 and P8_12
# //	Setup:  config-pin P9_16 pwm
# //			config-pin P8_11 eqep
# //			config-pin P8_12 eqep
# //	See:
# ////////////////////////////////////////
import time
import signal
import sys

# Set up encoder
eQEP = '2'
COUNTERPATH = '/dev/bone/counter/counter'+eQEP+'/count0'
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
pwm     = '1'  # pwm to use
channel = 'b'  # channel to use
PWMPATH='/dev/bone/pwm/'+pwm+'/'+channel
low  = 0.6 # Smallest angle (in ms)
hi   = 2.5 # Largest angle (in ms)
ms   = 250 # How often to change position, in ms
pos  = 1.5 # Current position, about middle ms)
step = 0.1 # Step size to next position

def signal_handler(sig, frame):
    print('Got SIGINT, turning motor off')
    f = open(PWMPATH+'/enable', 'w')
    f.write('0')
    f.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

f = open(PWMPATH+'/period', 'w')
f.write(pwmPeriod)
f.close()
f = open(PWMPATH+'/duty_cycle', 'w')
f.write(str(round(int(pwmPeriod)/2)))
f.close()
f = open(PWMPATH+'/enable', 'w')
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
		# print("data = " + data)
		# # map 0-180  to low-hi
		duty_cycle = -1*int(data)*(hi-low)/180.0 + hi
		duty_cycle = str(int(duty_cycle*1000000))	# Convert from ms to ns
		# print('duty_cycle = ' + duty_cycle)
		f = open(PWMPATH+'/duty_cycle', 'w')
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

# | Pin   | pwm | channel
# | P9_31 | 0   | a
# | P9_29 | 0   | b
# | P9_14 | 1   | a
# | P9_16 | 1   | b
# | P8_19 | 2   | a
# | P8_13 | 2   | b
