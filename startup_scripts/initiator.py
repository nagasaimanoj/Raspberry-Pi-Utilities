from multiprocessing import Process
from os import system


# parallel scripts
parallel_scripts = [
    'restart-press-simple.py',
    'shutdown-press-simple.py',
    'update_repo.py'
]

for each_script in parallel_scripts:
    Process(
        target=system,
        args=('python3 ' + each_script,)
    ).start()


# sequence scripts
sequence_scripts = [
    'update.py',
    'update_repo.py'
]

for each_script in sequence_scripts:
    system('python3 ' + each_script)
