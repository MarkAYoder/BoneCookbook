// //////////////////////////////////////
// 	toggle2.c
//  Toggles P9_14 and P9_16 pins as fast as it can. 
//	P9_14 and P9_16 are both on chip 1 so they can be toggled together.
//	P9_14 is line 18 P9_16 is line 18.
// 	Wiring:	Attach an oscilloscope to P9_14 and P9_16  to see the squarewave or 
//          uncomment the usleep and attach an LED.
// 	Setup:	sudo apt uupdate; sudo apt install libgpiod-dev
// 	See:	https://github.com/starnight/libgpiod-example/blob/master/libgpiod-led/main.c
// //////////////////////////////////////
#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

#define	CONSUMER	"Consumer"
#define NUMLINES 4

int main(int argc, char **argv)
{
	int chipnumber = 1;
	unsigned int line_num[NUMLINES] = {21, 22, 23, 24};	// USR LEDS 1-4
	unsigned int val;
	struct gpiod_chip *chip;
	struct gpiod_line_bulk line[NUMLINES];
	int i, ret;

	chip = gpiod_chip_open_by_number(chipnumber);
	if (!chip) {
		perror("Open chip failed\n");
		goto end;
	}

	int err = gpiod_chip_get_lines(chip, line_num, NUMLINES, line);
	if (err) {
		perror("Get line failed\n");
		goto close_chip;
	}

	int off_values[NUMLINES] = {0, 0, 0, 0};
	int  on_values[NUMLINES] = {1, 1, 1 ,1} ;
	ret = gpiod_line_request_bulk_output(line, CONSUMER, off_values);
	if (ret < 0) {
		perror("Request line as output failed\n");
		goto release_line;
	}

	/* Blink */
	val = 0;
	while(1) {
		ret = gpiod_line_set_value_bulk(line, val ? on_values : off_values);
		if (ret < 0) {
			perror("Set line output failed\n");
			goto release_line;
		}
		// printf("Output %u on line #%u\n", val, line_num);
		usleep(100000);
		val = !val;
	}

release_line:
	gpiod_line_release_bulk(line);
close_chip:
	gpiod_chip_close(chip);
end:
	return 0;
}
