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

    system('sudo init 0')


def restart():
    # GPIO_26 + GND  = restart

    log('waiting for restart trigger')
    Button(26).wait_for_press()

    system('sudo init 6')


def update_dir():
    # updates Utilities scripts

    git_dir_path = '/home/pi/GNSMK/Raspberry-Pi-Utilities'

    log('updating utilities dir')

    log('changing git dir')
    path_change_err = chdir('git_dir_path')

    git_result = os.system('git pull origin master')
    log('git result ' + git_result)

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
    log('starting ' + each_func.__name__ + 'func')

    Process(target=each_func).start()

    log(each_func.__name__ + ' func started')
