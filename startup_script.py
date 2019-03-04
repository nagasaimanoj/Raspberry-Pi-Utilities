from logging import DEBUG, basicConfig, debug
from multiprocessing import Process
from os import chdir, popen, system
from time import sleep

from gpiozero import Button

basicConfig(
    filename='/home/pi/GNSMK/natalie.log',
    level=DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log(message):
    print(message)
    debug(message)


def shutdown():
    # GPIO_21 + GND = shutdown

    log('waiting for shutdown trigger')
    Button(21).wait_for_press()

    log('shutdown triggered')
    system('sudo poweroff')


def restart():
    # GPIO_26 + GND  = reboot

    log('waiting for restart trigger')
    Button(26).wait_for_press()

    log('reboot triggered')
    system('sudo reboot')


def update_dir():
    # updates Utilities scripts

    git_dir_path = '/home/pi/GNSMK/Raspberry-Pi-Utilities'

    log('updating utilities dir')

    log('changing git dir')
    _ = chdir(git_dir_path)

    git_result = system('git pull origin master')
    log('git result ' + str(git_result))

    log('utilities dir updated')


def show_temp():
    # logs processor temperature for every second

    while True:
        temp = popen("vcgencmd measure_temp").readline()
        log('cpu_temp' + str(temp))

        sleep(1)


func_list = [
    restart,
    shutdown,
    update_dir,
    show_temp
]

for each_func in func_list:
    log(each_func.__name__ + '()')

    Process(target=each_func).start()

    log(each_func.__name__ + ' -- started')
