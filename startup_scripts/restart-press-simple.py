from os import system

from gpiozero import Button

button_26 = Button(26)

button_26.wait_for_press()
system("sudo init 6 \n")
