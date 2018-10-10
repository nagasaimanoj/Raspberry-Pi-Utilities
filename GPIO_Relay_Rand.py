from random import randint, random
from time import sleep

from RPi import GPIO

pins = [2, 3, 4, 14]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

while True:
    GPIO.output(
        pins[randint(0, 3)],
        randint(0, 1)
    )
    sleep(random())
