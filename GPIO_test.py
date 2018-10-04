from RPi import GPIO
import time

pins = [2, 3, 4, 14]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

while True:
    for each_pin in pins:
        time.sleep(0.5)
        GPIO.output(each_pin,  GPIO.LOW)

        time.sleep(0.5)
        GPIO.output(each_pin,  GPIO.HIGH)
