#!/usr/bin/env node
////////////////////////////////////////
//	externalLED.js
//	Blinks the P9_14 pin
//	Wiring:
//	Setup:  config-pin P9_14 pwm
//          cd /sys/class/pwm/pwmchip5
//          echo 0 > export
//	See:
////////////////////////////////////////
const fs = require("fs");
const ms = '20';    // Fade time in ms

const pwmPeriod = '1000000';    // Period in ns
const pwmchip = '5';  // pwm chip to use
const pwm = '0';      // pwm to use
const PWMPATH='/sys/class/pwm/pwmchip'+pwmchip;
var   step = 0.02;  // Step size
const min = 0.02,     // dimmest value
    max = 1;        // brightest value
var brightness = min; // Current brightness;


// fs.writeFileSync(PWMPATH+'/export', pwm);   // Export the pwm channel
// Set the period in ns, first 0 duty_cycle, 
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', '0');
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/period', pwmPeriod);
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', pwmPeriod/2);
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/enable', '1');

setInterval(fade, ms);      // Step every  ms

function fade() {
     fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', 
        parseInt(pwmPeriod*brightness));
    brightness += step;
    if(brightness >= max || brightness <= min) {
        step = -1 * step;
    }
}
