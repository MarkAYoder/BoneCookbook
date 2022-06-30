#!/usr/bin/env node
////////////////////////////////////////
//	pushbutton.js
//      Reads P9_42 and prints its value.
//	Wiring:	Connect a switch between P9_42 and 3.3V
//	Setup:	
//	See:	
////////////////////////////////////////
const fs = require("fs");

const pin = '7'; // P(_42 is gpio 7

GPIOPATH="/sys/class/gpio/";
// Make sure pin is exported
if(!fs.existsSync(GPIOPATH+"gpio"+pin)) {
    fs.writeFileSync(GPIOPATH+"export", pin);
}
// Make it an input pin
fs.writeFileSync(GPIOPATH+"gpio"+pin+"/direction", "in");

// Read every 500ms
setInterval(readPin, 500);

function readPin() {
    var data = fs.readFileSync(GPIOPATH+"gpio"+pin+"/value");
    console.log('data= ' + data);
 }
