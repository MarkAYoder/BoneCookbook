#!/usr/bin/env node
////////////////////////////////////////
//	pushbutton.js
//      Reads P9_42 and prints its value.
//	Wiring:	Connect a switch between P9_42 and 3.3V
//	Setup:	
//	See:	
////////////////////////////////////////
const fs = require("fs");

const ms = 500   // Read time in ms
const pin = '7'; // P9_42 is gpio 7
const GPIOPATH="/sys/class/gpio/";

// Make sure pin is exported
if(!fs.existsSync(GPIOPATH+"gpio"+pin)) {
    fs.writeFileSync(GPIOPATH+"export", pin);
}
// Make it an input pin
fs.writeFileSync(GPIOPATH+"gpio"+pin+"/direction", "in");

// Read every ms
setInterval(readPin, ms);

function readPin() {
    var data = fs.readFileSync(GPIOPATH+"gpio"+pin+"/value").slice(0, -1);
    console.log('data = ' + data);
 }
