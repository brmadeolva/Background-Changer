#!/usr/bin/env python3
import subprocess
import datetime
import random
from time import sleep
import os

n = []
while True:
    pack = 'null'
    pic = 0
    c = 0
    hour = datetime.datetime.now().hour
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    moda = f'{month}' + f'/{day}'
    list = [' ']
    number_files = len(list)

    c = c + 1
    list = os.listdir('Wallpapers')
    number_files = len(list)
    pic = random.randint(0, (number_files-1))

    subprocess.Popen(
        "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri "
        f"file://{f'/media/jakegwj/Files/backchanger/Wallpapers/{pic}.png'}", shell=True)

    print(f'[{date} {time}] Background set. (ID: {pic})')
    sleep(1800)
