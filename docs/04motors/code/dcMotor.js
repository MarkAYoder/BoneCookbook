#!/usr/bin/env node
////////////////////////////////////////
//	dcMotor.js
//	This is an example of driving a DC motor
//	Wiring:
//	Setup:  config-pin P9_16 pwm
//          cd /sys/class/pwm/pwmchip5
//          echo 1 > export
//          cd pwm1
//          chgrp gpio *
//          chmod g+w *
//	See:
////////////////////////////////////////
const fs = require("fs");

const pwmPeriod = '1000000';    // Period in ns
const pwmchip = '5';  // pwm chip to use
const pwm = '1';      // pwm to use
const PWMPATH='/sys/class/pwm/pwmchip'+pwmchip;

const min = 0.05,     // Slowest speed (duty cycle)
      max = 1,        // Fastest (always on)
      ms = 100;       // How often to change speed, in ms
var   speed = 0.5,    // Current speed;
      step = 0.05;    // Change in speed

// fs.writeFileSync(PWMPATH+'/export', pwm);   // Export the pwm channel
// Set the period in ns, first 0 duty_cycle, 
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', '0');
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/period', pwmPeriod);
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', pwmPeriod/2);
fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/enable', '1');

setInterval(sweep, ms);

function sweep() {
    speed += step;
    if(speed > max || speed < min) {
        step *= -1;
    }
    fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/duty_cycle', 
    parseInt(pwmPeriod*speed));
    console.log('speed = ' + speed);
}

process.on('SIGINT', function() {
    console.log('Got SIGINT, turning motor off');
    clearInterval(timer);       // Stop the timer
    fs.writeFileSync(PWMPATH+'/pwm'+pwm+'/enable', '0');
});