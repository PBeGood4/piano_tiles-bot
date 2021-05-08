#!/usr/bin/python3

import random
import mss
import mss.tools
import threading
import time
from pynput import mouse,keyboard
from pynput.mouse import Controller, Button

mouse = Controller()


def mainFunc(timeDelay):  
    global monitor
    offset=monitor["height"]-10
    sct_img = sct.grab(monitor)   
    if sct_img.pixel(int(monitor["width"]/4),int(monitor["height"]/10))[0]  <10:
            mouse.position = (int(monitor["width"]/8)  +int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset)
            time.sleep(1)
            mouse.click(Button.left)    
    elif sct_img.pixel(int(monitor["width"]/4*3),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*3) +int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset)
            time.sleep(1)
            mouse.click(Button.left)
    elif sct_img.pixel(int(monitor["width"]/4*5),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*5) +int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset)
            time.sleep(1)
            mouse.click(Button.left)
    elif sct_img.pixel(int(monitor["width"]/4*7),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*7) +int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset)
            time.sleep(1)
            mouse.click(Button.left)     

    while True:
        if a:
            break
        sct_img = sct.grab(monitor)

        if sct_img.pixel(int(monitor["width"]/4),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8)  +int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset)
            mouse.click(Button.left)    
        elif sct_img.pixel(int(monitor["width"]/4*3),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*3)+int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset)
            mouse.click(Button.left)
        elif sct_img.pixel(int(monitor["width"]/4*5),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*5)+int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset)
            mouse.click(Button.left)
        elif sct_img.pixel(int(monitor["width"]/4*7),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*7)+int(monitor["left"]),int(monitor["height"]/10)+monitor["top"]+offset  )
            mouse.click(Button.left)
  



a=False
pos1 = (0,0)
pos2 = (0,0)
def on_press(key):
    global offset
    if key == keyboard.Key.space:
        global pos1
        global pos2
        if pos1 ==(0,0):
            pos1 = mouse.position
            print("Position 1 = "+str(mouse.position))
        elif pos2 ==(0,0):
            pos2 = mouse.position 
            print("Position 2 = "+str(mouse.position))
            

    if key == keyboard.Key.shift_r   and offset+5<monitor["height"]:
        offset+=5
        print(offset)

    if key == keyboard.Key.shift and offset-5>  0:
        offset-=5
        print(offset)

def on_release(key):
    global a
    if key == keyboard.Key.esc:
        a=True
        return False

    


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
def listen():
    listener.join()

threading.Thread(target=listen).start()

print("\nSelect the boundaries\n\n1. Top Left\n2. Bottom Right\n")

while pos2==(0,0):
    pass

with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": pos1[1], "left": pos1[0], "width": (pos2[0]-pos1[0]), "height": (pos2[1]-pos1[1])}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

time.sleep(1)
print("\nPress ESC to exit\n  ")
time.sleep(1)
print("Starting in 5")
time.sleep(1)
print("Starting in 4")
time.sleep(1)
print("Starting in 3")
time.sleep(1)
print("Starting in 2")
time.sleep(1)
print("Starting in 1")
time.sleep(1)
print(".......")

mainFunc(0)







