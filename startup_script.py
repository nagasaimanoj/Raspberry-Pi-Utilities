import logging
import multiprocessing
import os
import time

import gpiozero

logging.basicConfig(
    filename='/home/pi/GNSMK/natalie.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log(message):
    print(message)
    logging.debug(message)


def shutdown():
    # GPIO_21 + GND = shutdown

    log('waiting for shutdown trigger')
    gpiozero.Button(21).wait_for_press()

    os.system('sudo init 0')


def restart():
    # GPIO_26 + GND  = restart

    log('waiting for restart trigger')
    gpiozero.Button(26).wait_for_press()

    os.system('sudo init 6')


def update_dir():
    # updates Utilities scripts

    git_dir_path = '/home/pi/GNSMK/Raspberry-Pi-Utilities'

    log('updating utilities dir')

    log('changing git dir')
    path_change_err = os.chdir('git_dir_path')

    if os.system('pwd') == git_dir_path:
        log('path change success')

        git_result = os.system('git pull origin master')

        log('utilities dir updated')
    else:
        log('path change fail' + path_change_err)


def show_temp():
    # logs processor temperature for every second

    while True:
        temp = os.popen("vcgencmd measure_temp").readline()
        log('cpu_temp' + str(temp))

        time.sleep(1)


func_list = [
    restart,
    shutdown,
    update_dir,
    show_temp
]

for each_func in func_list:
    log('starting ' + each_func.__name__)

    multiprocessing.Process(target=each_func).start()

    log(each_func.__name__ + 'started')
