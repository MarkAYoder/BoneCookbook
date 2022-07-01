#!/usr/bin/env python
# ////////////////////////////////////////
# //	i2cTemp.py
# //      Write an 8x8 Red/Green LED matrix.
# //	Wiring:	Attach to i2c as shown in text.
# //	Setup:	echo tmp101 0x49 > /sys/class/i2c-adapter/i2c-2/new_device
# //	See:	https://www.adafruit.com/product/902
# ////////////////////////////////////////
import smbus
import time

bus = smbus.SMBus(2)  # Use i2c bus 2       <1>
matrix = 0x70         # Use address 0x70    <2>
ms = 1;               # Delay between images in ms

# The first byte is GREEN, the second is RED.   <3>
smile = [0x00, 0x3c, 0x00, 0x42, 0x28, 0x89, 0x04, 0x85,
    0x04, 0x85, 0x28, 0x89, 0x00, 0x42, 0x00, 0x3c
]
frown = [0x3c, 0x00, 0x42, 0x00, 0x85, 0x20, 0x89, 0x00,
    0x89, 0x00, 0x85, 0x20, 0x42, 0x00, 0x3c, 0x00
]
neutral = [0x3c, 0x3c, 0x42, 0x42, 0xa9, 0xa9, 0x89, 0x89,
    0x89, 0x89, 0xa9, 0xa9, 0x42, 0x42, 0x3c, 0x3c
]

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10) <4>
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

bus.write_i2c_block_data(matrix, 0, frown)      # <5>
for fade in range(0xef, 0xe0, -1):              # <6>
    bus.write_byte_data(matrix, fade, 0)
    time.sleep(ms/10)

bus.write_i2c_block_data(matrix, 0, neutral)
for fade in range(0xe0, 0xef, 1):
    bus.write_byte_data(matrix, fade, 0)
    time.sleep(ms/10)

bus.write_i2c_block_data(matrix, 0, smile)
