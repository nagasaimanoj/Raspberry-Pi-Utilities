from multiprocessing import Process
from os import system

from gpiozero import Button


def restart():
    # restart on sorting GPIO 26 with GND
    Button(26).wait_for_press()
    system("sudo init 6 \n")


def shutdown():
    # shutdown on sorting GPIO 21 with GND
    Button(21).wait_for_press()
    system("sudo init 0 \n")


def update_repo():
    # updates the current repo with remote repo
    system('cd /hpme/pi/GNSMK/Raspberry-Pi-Utilities/ \n')
    system('git pull origin master \n')


Process(target=restart).start()
Process(target=shutdown).start()
Process(target=update_repo).start()
