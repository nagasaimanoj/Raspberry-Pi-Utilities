import os

try:
    from gpiozero import Button

    Button(21).wait_for_press()
    os.system("python neural_network_infinate.py\n")
    # os.system("sudo poweroff")
except Exception as e:
    open('console_log.txt', 'a').write(str(e))
