from os import popen
from time import sleep

while True:
    temp = popen("vcgencmd measure_temp").readline()
    print(temp)

    sleep(1)
