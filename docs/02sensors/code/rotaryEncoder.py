#!/usr/bin/env python
# // This uses the eQEP hardware to read a rotary encoder
# // bone$ config-pin P8_11 eqep
# // bone$ config-pin P8_12 eqep
import time
    
eQEP = '2'
COUNTERPATH = '/dev/bone/counter/counter'+eQEP+'/count0'
	
ms = 100 	# Time between samples in ms
maxCount = '1000000'

# Set the eEQP maximum count
f = open(COUNTERPATH+'/ceiling', 'w')
f.write(maxCount)
f.close()

# Enable
f = open(COUNTERPATH+'/enable', 'w')
f.write('1')
f.close()

f = open(COUNTERPATH+'/count', 'r')

olddata = -1
while True:
	f.seek(0)
	data = f.read()[:-1]
	# Print only if data changes
	if data != olddata:
		olddata = data
		print("data = " + data)
	time.sleep(ms/1000)

# Black OR Pocket
# eQEP0:	P9.27 and P9.42 OR P1_33 and P2_34
# eQEP1:	P9.33 and P9.35
# eQEP2:	P8.11 and P8.12 OR P2_24 and P2_33

# AI
# eQEP1:	P8.33 and P8.35
# eQEP2:	P8.11 and P8.12 or P9.19 and P9.41
# eQEP3:	P8.24 abd P8.25 or P9.27 and P9.42