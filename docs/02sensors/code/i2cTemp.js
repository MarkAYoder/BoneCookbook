#!/usr/bin/env node
////////////////////////////////////////
//	i2cTemp.js
//      Read at TMP101 sensor on i2c bus 2, address 0x49
//	Wiring:	Attach to i2c as shown in text.
//	Setup:	echo tmp101 0x49 > /sys/class/i2c-adapter/i2c-2/new_device
//	See:	
////////////////////////////////////////
const fs = require("fs");

const ms = 1000;   // Read time in ms
const bus = '2';
const addr = '49';
I2CPATH='/sys/class/i2c-adapter/i2c-'+bus+'/'+bus+'-00'+addr+'/hwmon/hwmon0';

// Read every ms
setInterval(readTMP, ms);

function readTMP() {
    var data = fs.readFileSync(I2CPATH+"/temp1_input").slice(0, -1);
    console.log('data (C) = ' + data/1000);
 }
