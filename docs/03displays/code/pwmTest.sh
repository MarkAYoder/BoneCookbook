#!/usr/bin/env bash

# config-pin P9_14 pwm

PWMPATH=/sys/class/pwm

echo Testing pwmchip$1 pwm$2 in
echo $PWMPATH/pwmchip$1


cd $PWMPATH/pwmchip$1
sudo chgrp gpio *
sudo chmod g+w *
echo $2 > export

cd pwm$2
sudo chgrp gpio *
sudo chmod g+w *
ls -ls
echo 1000000000 > period
echo  500000000 > duty_cycle
echo  1 > enable