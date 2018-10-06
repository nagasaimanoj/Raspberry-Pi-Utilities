import time

from RPi import GPIO

pins = [2, 3, 4, 14]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

while True:
    for each_pin in pins:
        GPIO.output(each_pin,  GPIO.LOW)

        time.sleep(0.5)
        GPIO.output(each_pin,  GPIO.HIGH)
