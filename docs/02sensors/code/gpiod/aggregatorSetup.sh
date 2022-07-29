# See:  https://elinux.org/EBC_Exercise_51_GPIO_aggregator

# Insert the module
sudo modprobe gpio-aggregator
# Go to the aggregator
cd /sys/bus/platform/drivers/gpio-aggregator
# Fix the modes
sudo chgrp gpio *
sudo chmod g+w *
# See what's there before adding a new chip
gpiodetect 
# gpiochip0 [gpio-0-31] (32 lines)
# gpiochip1 [gpio-32-63] (32 lines)
# gpiochip2 [gpio-64-95] (32 lines)
# gpiochip3 [gpio-96-127] (32 lines)

# Add a new chip mapping P9_14, P9_16, P9_18 and P9_22
gpioinfo | grep -e chip -e P9_1[468] -e P9_22
# gpiochip0 - 32 lines:
# 	line   2: "P9_22 [spi0_sclk]" "gpio-aggregator.0" input active-high [used]
# 	line   4: "P9_18 [spi0_d1]" "gpio-aggregator.0" output active-high [used]
# gpiochip1 - 32 lines:
# 	line  18: "P9_14 [ehrpwm1a]" "gpio-aggregator.0" output active-high [used]
# 	line  19: "P9_16 [ehrpwm1b]" "gpio-aggregator.0" input active-high [used]
# gpiochip2 - 32 lines:
# gpiochip3 - 32 lines:

echo "gpio-32-63 18,19 gpio-0-31 4,2" > new_device
# Check to see if they are there
gpiodetect 
# gpiochip0 [gpio-0-31] (32 lines)
# gpiochip1 [gpio-32-63] (32 lines)
# gpiochip2 [gpio-64-95] (32 lines)
# gpiochip3 [gpio-96-127] (32 lines)
# gpiochip4 [gpio-aggregator.0] (4 lines)

gpioinfo | tail -6
# 	line  31:         "NC"       unused   input  active-high 
# gpiochip4 - 4 lines:
# 	line   0:      unnamed       unused  output  active-high 
# 	line   1:      unnamed       unused   input  active-high 
# 	line   2:      unnamed       unused   input  active-high 
# 	line   3:      unnamed       unused  output  active-high 

# Turn them all on, then off
gpioset gpiochip4 0=1 1=1 2=1 3=1
gpioset gpiochip4 0=0 1=0 2=0 3=0
