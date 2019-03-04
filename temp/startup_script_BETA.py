from logging import DEBUG, basicConfig, debug
from os import chdir, system

from gpiozero import Button

basicConfig(
    filename='/home/pi/GNSMK/natalie.log',
    level=DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Boottime Programs
Button(21, hold_time=10).when_held = lambda: (
    debug('shutdown triggered'),
    system('sudo shutdown -h now')
)

Button(26, hold_time=10).when_held = lambda: (
    debug('reboot triggered'),
    system('sudo reboot')
)

Button(20).when_pressed = lambda: (
    debug('update triggered'),

    chdir('/home/pi/GNSMK/Raspberry-Pi-Utilities'),
    system('git pull origin master'),

    debug(system('git pull origin master'))
)
