from multiprocessing import Process
from os import system

from gpiozero import Button


def restart():
    Button(26).wait_for_press()
    system("sudo init 6 \n")


def shutdown():
    Button(21).wait_for_press()
    system("sudo init 0 \n")


p1 = Process(target=restart)
p2 = Process(target=shutdown)

p1.start()
p2.start()
