#!/usr/bin/python3

import random
import cv2 as cv
import pyautogui
import mss
import mss.tools
import threading
import time
from pynput import mouse,keyboard
from pynput.mouse import Controller, Button
import sys

sys.platform ="_"


mouse = Controller()
  

    

def mainFunc(timeDelay):        
    while True:
        if a:
            break
        sct_img = sct.grab(monitor)

        if sct_img.pixel(int(monitor["width"]/4),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8)  ,int(monitor["height"]/10)+monitor["top"]+70)
            mouse.click(Button.left)    
        elif sct_img.pixel(int(monitor["width"]/4*3),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*3),int(monitor["height"]/10)+monitor["top"]+70)
            mouse.click(Button.left)
        elif sct_img.pixel(int(monitor["width"]/4*5),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*5),int(monitor["height"]/10)+monitor["top"]+70)
            mouse.click(Button.left)
        elif sct_img.pixel(int(monitor["width"]/4*7),int(monitor["height"]/10))[0]<10:
            mouse.position = (int(monitor["width"]/8*7),int(monitor["height"]/10)+monitor["top"]+70  )
            mouse.click(Button.left)



a=False
spaceTimes=0
pos1 = (0,0)
pos2 = (0,0)
def on_press(key):
    if key == keyboard.Key.space:
        global spaceTimes
        global pos1
        global pos2
        global pos3
        global pos4
        spaceTimes+=1
        if pos1 ==(0,0):
            pos1 = mouse.position
            print("Position 1 = "+str(mouse.position))
        elif pos2 ==(0,0):
            pos2 = mouse.position 
            print("Position 2 = "+str(mouse.position))

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

while pos2==(0,0):
    pass

with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": pos1[1], "left": pos1[0], "width": (pos2[0]-pos1[0]), "height": (pos2[1]-pos1[1])}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

time.sleep(1)
print("Starting...")
mainFunc(0)




