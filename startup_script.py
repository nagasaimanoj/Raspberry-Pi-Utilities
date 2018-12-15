import logging
import multiprocessing
import os
import time

import gpiozero

logging.basicConfig(
    filename='natalie',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def shutdown():
    # GPIO_21 + GND = shutdown
    gpiozero.Button(21).wait_for_press()
    logging.debug('waiting for shutdown trigger')

    os.system('sudo init 0')


def restart():
    # GPIO_26 + GND  = restart
    gpiozero.Button(26).wait_for_press()
    logging.debug('waiting for restart trigger')

    os.system('sudo init 6')


def update_dir():
    # updates Utilities scripts
    os.chdir('/home/pi/GNSMK/Raspberry-Pi-Utilities')
    logging.debug('cwd is not git dir')

    git_result = os.system('git pull origin master')
    logging.info('git_result : ' + git_result)


def show_temp():
    # prints processor temperature for every second
    while True:
        temp = os.popen("vcgencmd measure_temp").readline()
        logging.debug('cpu_temp' + temp)

        time.sleep(1)


func_list = [
    restart,
    shutdown,
    update_dir,
    show_temp
]

for each_func in func_list:
    multiprocessing.Process(target=each_func).start()
