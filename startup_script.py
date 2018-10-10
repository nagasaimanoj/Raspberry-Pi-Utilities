from multiprocessing import Process
from os import system

from gpiozero import Button


def shutdown():
    # GPIO_21 + GND = shutdown
    Button(21).wait_for_press()
    system('sudo init 0')


def restart():
    # GPIO_26 + GND  = restart
    Button(26).wait_for_press()
    system('sudo init 6')


def update_dir():
    # updates Utilities scripts
    system('cd /home/pi/GNSMK/Raspberry-Pi-Utilities')
    system('git pull origin master')


Process(target=restart).start()
Process(target=shutdown).start()
Process(target=update_dir).start()
