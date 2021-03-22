"""
A simple script that schedules changing your wallpaper on
ubuntu operating system.
Pictures for the wallpaper should be in directory
specified in *wallpaper_dir*.
Wallpaper change threshold is specified in *minutes* variable.
"""

import os
import random
import time

wallpaper_dir = '/home/michal/Pictures/wallpaper/'
minutes = 5

while True:
    time.sleep(minutes * 60)

    pics = os.listdir(wallpaper_dir)
    pic = random.choice(pics)
    command = f'gsettings set org.gnome.desktop.background picture-uri {wallpaper_dir}/{pic}'
    os.system(command)
