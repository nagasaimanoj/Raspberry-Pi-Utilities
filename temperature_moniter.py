import os
import time

while True:
    temp = os.popen("vcgencmd measure_temp").readline()
    print(temp.replace("temp=", ""))
    time.sleep(1)
