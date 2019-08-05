import random
import time
import keyboard
from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Button, Controller
import win32api, win32con
import threading

mouse = Controller()
started = False
def Start(afk):
    keys = ['e','shift','q', '3',
            'g', 'j', 'k', 'b', 'n', 'x', 'z']
    movement = ['w', 'a', 's', 'd', 'space', 'ctrl']
    while afk:
        #win32api.SetCursorPos((random.randrange(1, 1000),random.randrange(1, 1000)))
        randomKey = random.choice(keys)
        randomMove = random.choice(movement)
        randomMovee = random.choice(movement)
        timeDelay = random.randrange(0, 2)
        
        print(randomKey)
        
        keyboard.press(randomKey)
        keyboard.press(randomMove)
        keyboard.press(randomMovee)
        mouse.press(Button.left)
        
        time.sleep(timeDelay)
        
        mouse.release(Button.left)
        keyboard.release(randomKey)
        keyboard.release(randomMove)
        keyboard.release(randomMovee)

def on_press(key):
    global started
    if key == Key.f1:
        if started == False:
            print("started || ", started)
            Start(True)
        else:
            print("stopped || ", started)
            started = False
            Start(False)
            
with Listener(on_press=on_press) as listener:
    listener.join()

