import pythoncom
import keyboard
from pynput.keyboard import Key, Controller, Listener
import time
print('Press Capslock to get close to your teammate and release it to superjump :)')
def on_press(key):
    #print('{0} pressed'.format(key))
    if key == Key.caps_lock:
        keyboard.press('ctrl')
        keyboard.press('shift')
       
def on_release(key):
    #print('{0} release'.format(key))
    if key == Key.caps_lock:
        keyboard.release('ctrl')
        keyboard.release('shift')
        keyboard.press('space')
        keyboard.release('space')
        
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

