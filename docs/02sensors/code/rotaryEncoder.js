#!/usr/bin/env node
// This uses the eQEP hardware to read a rotary encoder
// bone$ config-pin P8_11 qep
// bone$ config-pin P8_12 qep

const fs = require("fs");
    
const eQEP = "2";
const COUNTERPATH = '/sys/bus/counter/devices/counter'+eQEP+'/count0';
	
const ms = 250; 	// Time between samples in ms
const maxCount = '1000000';

// Set the eEQP maximum count
fs.writeFileSync(COUNTERPATH+'/ceiling', maxCount);

// Enable
fs.writeFileSync(COUNTERPATH+'/enable', '1');

setInterval(readEncoder, ms);    // Check state every 250 ms

function readEncoder() {
	var data = fs.readFileSync(COUNTERPATH + '/count').slice(0, -1);
	console.log('data= ' + data);
}

// Black OR Pocket
// eQEP0:	P9.27 and P9.42 OR P1_33 and P2_34
// eQEP1:	P9.33 and P9.35
// eQEP2:	P8.11 and P8.12 OR P2_24 and P2_33

// AI
// eQEP1:	P8.33 and P8.35
// eQEP2:	P8.11 and P8.12 or P9.19 and P9.41
// eQEP3:	P8.24 abd P8.25 or P9.27 and P9.42