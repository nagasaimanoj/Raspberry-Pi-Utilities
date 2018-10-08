from time import sleep
from random import random

from RPi import GPIO

pins = [2, 3, 4, 14]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

while True:
    for each_pin in pins:
        GPIO.output(each_pin,  int(random()))
        sleep(0.5)
