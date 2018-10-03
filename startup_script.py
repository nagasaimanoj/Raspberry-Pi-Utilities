from multiprocessing import Process
from os import system

from gpiozero import Button


def restart():
    Button(26).wait_for_press()
    system("sudo init 6 \n")


def shutdown():
    Button(21).wait_for_press()
    system("sudo init 0 \n")


def update_repo():
    system('cd /hpme/pi/GNSMK/Raspberry-Pi-Utilities/ \n')
    system('git pull origin master \n')


def update_linux():
    system('sudo apt-get update \n')
    system('sudo apt-get upgrade -y \n')
    system('sudo apt-get dist-upgrade -y \n')


Process(target=restart).start()
Process(target=shutdown).start()
Process(target=update_repo).start()
Process(target=update_linux).start()
