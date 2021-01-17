import time as ti
import keyboard
def clock():
    while True:
        print("The time is:")
        print(ti.asctime(ti.localtime()), end=\r, flush=True)
        if keyboard.is_pressed('s'):
            break
