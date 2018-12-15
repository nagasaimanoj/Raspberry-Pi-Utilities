from sys import argv
from time import sleep

from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_pin = int(argv[1])
GPIO.setup(GPIO_pin, GPIO.OUT)

current_state = not GPIO.input(GPIO_pin)

print(int(current_state))
