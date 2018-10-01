from os import system
from gpiozero import Button

button_21 = Button(21)

button_21.wait_for_press()
system("sudo init 0")
