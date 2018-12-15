from sys import argv
from time import sleep

from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_pin = int(argv[1])
GPIO_status = int(argv[2])

GPIO.setup(GPIO_pin, GPIO.OUT)

GPIO.output(GPIO_pin, GPIO_status)
