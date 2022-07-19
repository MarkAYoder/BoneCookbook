#!/usr/bin/env node
////////////////////////////////////////
//	externalLED.js
//	Blinks the P9_14 pin
//	Wiring:
//	Setup:
//	See:
////////////////////////////////////////
const fs = require("fs");

// Look up P9.14 using gpioinfo | grep -e chip -e P9.14.  chip 1, line 18 maps to 50
pin="50";

GPIOPATH="/sys/class/gpio/";
// Make sure pin is exported
if(!fs.existsSync(GPIOPATH+"gpio"+pin)) {
    fs.writeFileSync(GPIOPATH+"export", pin);
}
// Make it an output pin
fs.writeFileSync(GPIOPATH+"gpio"+pin+"/direction", "out");

// Blink every 500ms
setInterval(toggle, 500);

state="1";
function toggle() {
    fs.writeFileSync(GPIOPATH+"gpio"+pin+"/value", state);
    if(state == "0") {
        state = "1";
    } else {
        state = "0";
    }
}
