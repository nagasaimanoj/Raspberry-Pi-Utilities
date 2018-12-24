import logging
import multiprocessing
import os
import time

import git
import gpiozero

logging.basicConfig(
    filename='natalie.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def shutdown():
    # GPIO_21 + GND = shutdown

    logging.debug('waiting for shutdown trigger')
    gpiozero.Button(21).wait_for_press()

    os.system('sudo init 0')


def restart():
    # GPIO_26 + GND  = restart

    logging.debug('waiting for restart trigger')
    gpiozero.Button(26).wait_for_press()

    os.system('sudo init 6')


def update_dir():
    # updates Utilities scripts

    repo = git.Repo('/home/pi/GNSMK/Raspberry-Pi-Utilities/')
    repo.remotes.origin.pull()


def show_temp():
    # logs processor temperature for every second

    while True:
        temp = os.popen("vcgencmd measure_temp").readline()
        logging.debug('cpu_temp' + str(temp))

        time.sleep(1)


func_list = [
    restart,
    shutdown,
    update_dir,
    show_temp
]

for each_func in func_list:
    logging.info('starting ' + each_func.__name__)

    multiprocessing.Process(target=each_func).start()

    logging.info(each_func.__name__ + 'started')
