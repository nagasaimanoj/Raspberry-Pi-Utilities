from os import system

cmd_list = [
    'update',
    'upgrade -y',
    'dist-upgrade -y'
]

for each_cmd in cmd_list:
    system('sudo apt-get ' + each_cmd)
