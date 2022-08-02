#!/usr/bin/env python
import time
import os
import signal
import sys

# Motor is attached here
# controller = ["P9_11", "P9_13", "P9_15", "P9_17"]; 
# controller = ["30", "31", "48", "5"]
# controller = ["P9_14", "P9_16", "P9_18", "P9_22"]; 
controller = ["50", "51", "4", "2"]
states = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]
statesHiTorque = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]
statesHalfStep = [[1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0],
                      [0,0,1,0], [0,0,1,1], [0,0,0,1], [1,0,0,1]]

curState = 0    # Current state
ms = 250        # Time between steps, in ms
maxStep = 22    # Number of steps to turn before turning around
minStep = 0     # minimum step to turn back around on

CW  =  1       # Clockwise
CCW = -1
pos =  0       # current position and direction
direction = CW
GPIOPATH="/sys/class/gpio"

def signal_handler(sig, frame):
    print('Got SIGINT, turning motor off')
    for i in range(len(controller)) :
        f = open(GPIOPATH+"/gpio"+controller[i]+"/value", "w")
        f.write('0')
        f.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Hit ^C to stop')

def move():
    global pos
    global direction
    global minStep
    global maxStep
    pos += direction
    print("pos: " + str(pos))
    # Switch directions if at end.
    if (pos >= maxStep or pos <= minStep) :
        direction *= -1
    rotate(direction)

# This is the general rotate
def rotate(direction) :
    global curState
    global states
	# print("rotate(%d)", direction);
    # Rotate the state acording to the direction of rotation
    curState +=  direction
    if(curState >= len(states)) :
        curState = 0;
    elif(curState<0) :
        curState = len(states)-1
    updateState(states[curState])

# Write the current input state to the controller
def updateState(state) :
    global controller
    print(state)
    for i in range(len(controller)) :
        f = open(GPIOPATH+"/gpio"+controller[i]+"/value", "w")
        f.write(str(state[i]))
        f.close()

# Initialize motor control pins to be OUTPUTs
for i in range(len(controller)) :
    # Make sure pin is exported
    if (not os.path.exists(GPIOPATH+"/gpio"+controller[i])):
        f = open(GPIOPATH+"/export", "w")
        f.write(pin)
        f.close()
    # Make it an output pin
    f = open(GPIOPATH+"/gpio"+controller[i]+"/direction", "w")
    f.write("out")
    f.close()

# Put the motor into a known state
updateState(states[0])
rotate(direction)

# Rotate
while True:
    move()
    time.sleep(ms/1000)
