import os
import random
import time

wallpaper_dir = '/home/michal/Pictures/wallpaper/'

while True:
    minutes = 0.1
    time.sleep(minutes * 60)

    pics = os.listdir(wallpaper_dir)
    pic = random.choice(pics)
    command = f'gsettings set org.gnome.desktop.background picture-uri {wallpaper_dir}/{pic}'
    os.system(command)
