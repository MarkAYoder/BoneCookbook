////////////////////////////////////////
//	blinkLED.c
//	Blinks the P9_14 pin
//	Wiring:
//	Setup:
//	See:
////////////////////////////////////////
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#define MAXSTR 100
// Look up P9.14 using show-pins.  gpio1.18 maps to 50
int main() {
  FILE *fp;
  char pin[] = "50";
  char GPIOPATH[] = "/sys/class/gpio/";
  char path[MAXSTR] = "";

  // Make sure pin is exported
  snprintf(path, MAXSTR, "%s%s%s", GPIOPATH, "gpio", pin);
  // printf("%s\n", path);
  if (!access(path, F_OK) == 0) {
    snprintf(path, MAXSTR, "%s%s", GPIOPATH, "export");
    // printf("path: %s\n", path);
    fp = fopen(path, "w");
    fwrite(pin, sizeof(pin), strlen(pin), fp);
    fclose(fp);
  }
 
  // Make it an output pin
  snprintf(path, MAXSTR, "%s%s%s%s", GPIOPATH, "gpio", pin, "/direction");
  // printf("path: %s\n", path);
  fp = fopen(path, "w");
  fwrite("out", sizeof("out"), strlen("out"), fp);
  fclose(fp);

  // Blink every 500ms
  int state = 0;
  snprintf(path, MAXSTR, "%s%s%s%s", GPIOPATH, "gpio", pin, "/value");
  fp = fopen(path, "w");
  while (1) {
    fseek(fp, 0, SEEK_SET);
    if (state) {
      fwrite("1", sizeof("1"), strlen("1"), fp);
    } else {
      fwrite("0", sizeof("1"), strlen("1"), fp);
    }
    state = ~state;
    usleep(100000);   // sleep time in microseconds
  }
}