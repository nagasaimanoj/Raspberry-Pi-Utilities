from time import sleep

from RPi import GPIO

pins = [2, 3, 4, 14]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

while True:
    for each_pin in pins:
        GPIO.output(each_pin,  True)
        sleep(0.5)
        GPIO.output(each_pin,  False)
