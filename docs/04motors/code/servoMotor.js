#!/usr/bin/env node
////////////////////////////////////////
//	servoMotor.js
//	Drive a simple servo motor back and forth on P9_16 pin
//	Wiring:
//	Setup:  config-pin P9_16 pwm
//          cd /sys/class/pwm/pwmchip5
//          echo 1 > export
//          cd pwm1
//          chgrp Blinks thegpio *
//          chmod g+w *
//	See:
////////////////////////////////////////
const fs = require("fs");

const pwmPeriod = '20000000';    // Period in ns, (20 ms)
const pwmchip = '5';  // pwm chip to use
const pwm = '1';      // pwm to use
const PWMPATH='/sys/class/pwm/pwmchip'+pwmchip;
const min  = 0.8, // Smallest angle (in ms)
      max  = 2.4, // Largest angle (in ms)
      ms  = 250;  // How often to change position, in ms
var   pos = 1.5,  // Current position, about middle ms)
      step = 0.1; // Step size to next position

console.log('Hit ^C to stop');
// fs.writeFileSync(PWMPATH+'/export', pwm);   // Export the pwm channel
// Set the period in ns, first 0 duty_cycle, 
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', '0');
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/period', pwmPeriod);
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', pwmPeriod/2);
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/enable', '1');

var timer = setInterval(sweep, ms);

// Sweep from min to max position and back again
function sweep() {
    pos += step;    // Take a step
    if(pos > max || pos < min) {
        step *= -1;
    }
    var dutyCycle = parseInt(pos*1000000);    // Convert ms to ns
    // console.log('pos = ' + pos + ' duty cycle = ' + dutyCycle);
    fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', dutyCycle);
}

process.on('SIGINT', function() {
    console.log('Got SIGINT, turning motor off');
    clearInterval(timer);             // Stop the timer
    fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/enable', '0');
});

// | Pin   | pwmchip | pwm
// | P9_31 | 3       | 0
// | P9_29 | 3       | 1
// | P9_14 | 5       | 0
// | P9_16 | 5       | 1
// | P8_19 | 7       | 0
// | P8_13 | 7       | 1