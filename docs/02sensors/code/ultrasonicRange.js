#!/usr/bin/env node
//////////////////////////////////////
//	ultrasonicRange.js
// 	Reads the analog value of the sensor.
//////////////////////////////////////
const fs = require("fs");
const ms = 250;  // Time in milliseconds

const pin = "0";        // sensor, A0, P9_39

const IIOPATH='/sys/bus/iio/devices/iio:device0/in_voltage'+pin+'_raw';

console.log('Hit ^C to stop');

// Read every ms
setInterval(readPin, ms);

function readPin() {
    var data = fs.readFileSync(IIOPATH);
    console.log('data= ' + data);
 }
// Bone  | Pocket | AIN
// ----- | ------ | --- 
// P9_39 | P1_19  | 0
// P9_40 | P1_21  | 1
// P9_37 | P1_23  | 2
// P9_38 | P1_25  | 3
// P9_33 | P1_27  | 4
// P9_36 | P2_35  | 5
// P9_35 | P1_02  | 6
