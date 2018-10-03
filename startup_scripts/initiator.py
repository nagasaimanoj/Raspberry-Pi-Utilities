from multiprocessing import Process
from os import system

# running system update on startup
system('python update.py')

# all startup scripts
script_list = [
    'restart-press-simple.py',
    'shutdown-press-simple.py'
]

# running startup apps as parallel processes
for each_script in script_list:
    Process(
        target=system,
        args=('python3 ' + each_script,)
    ).start()
