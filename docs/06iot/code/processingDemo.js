var canvas = document.getElementById("mysketch");
var p = new Processing(canvas, sketchProc);

function sketchProc(pjs) {
    // Sketch global variables
    var radius = 50.0;
    var X, Y;
    var nX, nY;
    var delay = 16;
    var brightness = 0;
    var buttonStatus = 0;
    var sliderStatus = 0;
    var lastSliderValue = 0;
    var BUTTON = 'P8_19';
    var POT = 'P9_36';

    // Get the BoneScript library and begin updating the canvas
    setTargetAddress('beaglebone.local', {
        initialized: run
    });
    setTargetAddress('192.168.7.2', {
        initialized: run
    });

    function run() {
        var b = require('bonescript');
        b.pinMode(BUTTON, b.INPUT);

        // Setup the Processing Canvas
        pjs.setup = function () {
            pjs.size(256, 256);
            pjs.strokeWeight(10);
            pjs.frameRate(15);
            X = pjs.width / 2;
            Y = pjs.height / 2;
            nX = X;
            nY = Y;
        }

        // Main draw loop
        pjs.draw = function () {
            // Calculate some fading values based on the frame count
            radius = 50.0 + (15 - sliderStatus) * pjs.sin(pjs.frameCount / 4);
            brightness = (radius - 40.0) / 20.0;

            // Track circle to new destination
            X += (nX - X) / delay;
            Y += (nY - Y) / delay;

            // Fill canvas grey
            pjs.background(100);

            // Set fill-color to blue or red, based on button status
            if (buttonStatus) pjs.fill(200, 30, 20)
            else pjs.fill(0, 121, 184);

            // Set stroke-color white
            pjs.stroke(255);

            // Draw circle
            pjs.ellipse(X, Y, radius, radius);

            // Fetch slider location for next time
            b.analogRead(POT, onAnalogRead);

            // Fetch button status
            b.digitalRead(BUTTON, onDigitalRead);
        }

        // Get things started
        pjs.setup();

        // Handle data back from potentiometer
        function onAnalogRead(x) {
            if (!x.err && (x.value >= 0) && (x.value <= 1)) {
                if (Math.abs(x.value - lastSliderValue) > 0.05) {
                    lastSliderValue = x.value;
                    nY = x.value * 255;
                    sliderStatus = parseInt(x.value * 10, 10);
                }
            }
        }

        // Handle data back from button
        function onDigitalRead(x) {
            buttonStatus = (x.value == b.LOW) ? 1 : 0;
        }
    }
}