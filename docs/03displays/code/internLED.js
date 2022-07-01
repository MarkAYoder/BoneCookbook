#!/usr/bin/env node
// //////////////////////////////////////
// 	internalLED.js
// 	Blinks the USR LEDs.
// 	Wiring:
// 	Setup:
// 	See:
// //////////////////////////////////////
const fs = require('fs');
const ms = 250;     // Blink time in ms
const LED = 'usr0'; // LED to blink
const LEDPATH = '/sys/class/leds/beaglebone:green:'+LED+'/brightness';

var state = '1';    // Initial state

setInterval(flash, ms);    // Change state every ms

function flash() {
    fs.writeFileSync(LEDPATH, state)
    if(state === '1') {
        state = '0';
    } else {
        state = '1';
    }
}
