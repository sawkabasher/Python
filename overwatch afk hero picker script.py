import json
import time 
import threading
import keyboard
from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Button, Controller
import pyttsx3
from gtts import gTTS
import playsound
import os.path

with open('heroes.json', 'r') as f:
    heroes_dict = json.load(f)

for hero in heroes_dict:
    print(hero['Name'], hero['x_pos'], hero['y_pos'])

print(len(heroes_dict))
print(heroes_dict[1]['Name'])


profile = heroes_dict[0]
print(profile['x_pos'])


start_stop_key = Key.f2
show_mouse_position_key = Key.f3
switch_profile_key = Key.f4
exit_key = Key.f12

if os.path.exists('sounds'):
    for hero in heroes_dict:
        if os.path.isfile('sounds\{}.mp3'.format(hero['Name'])):
            pass
        else:
            
            tts = gTTS(text=hero['Name'], lang="en")
            tts.save('sounds\{}.mp3'.format(hero['Name']))
            print('{}.mp3 created !!!'.format(hero['Name']))
    pass
else:
    os.mkdir('sounds')
    tts = gTTS(text="press F4 to switch between profiles and press F2 to start", lang="en")
    tts.save('sounds\welcome.mp3')
    print('welcome.mp3 created !!!')
    
    tts = gTTS(text="start", lang="en")
    tts.save('sounds\start.mp3')
    print('start.mp3 created !!!')
    
    tts = gTTS(text="stop", lang="en")
    tts.save('sounds\stop.mp3')
    print('stop.mp3 created !!!')
    
    for hero in heroes_dict:
        tts = gTTS(text=hero['Name'], lang="en")
        tts.save('sounds\{}.mp3'.format(hero['Name']))
        print('{}.mp3 created !!!'.format(hero['Name']))
        
mouse = Controller()

class Main(threading.Thread):
    
    def __init__(self):
        print('press F4 to switch between profiles and press F2 to start')
        print (profile)

        playsound.playsound('sounds\welcome.mp3', False)
        time.sleep(4)
        playsound.playsound('sounds\{}.mp3'.format(profile['Name']),False)
        
        super(Main, self).__init__()
        self.running = False
        self.program_running = True
        
    def start_clicking(self):
        self.running = True
        
        
    def stop_clicking(self):
        self.running = False
        
    def exit(self):
        self.stop_clicking()
        self.program_running = False
    
    def run(self):
        while self.program_running:
            while self.running:
                print(profile)
                mouse.position = (profile['x_pos'],profile['y_pos'])
                mouse.click(Button.left,2)
                time.sleep(0.3)

main_thread = Main()
main_thread.start()

def on_press(key):
    global profile
    
    if key == start_stop_key:
        
        if main_thread.running:
            main_thread.stop_clicking()
            print('if main_thread.running == True')
            playsound.playsound('sounds\stop.mp3', False)
        else:
            main_thread.start_clicking()
            print('if main_thread.running == False')
            playsound.playsound('sounds\start.mp3', False)
    elif key == exit_key:
        main_thread.exit5listener.stop()
    elif key == show_mouse_position_key:
        print(mouse.position)
   
    elif key == switch_profile_key:
        
        if heroes_dict.index(profile) < (len(heroes_dict) - 1):
            profile = heroes_dict[heroes_dict.index(profile) + 1]
        else:
            profile = heroes_dict[0]
        playsound.playsound('sounds\{}.mp3'.format(profile["Name"]), False)
        print('{}/{}'.format(heroes_dict.index(profile), len(heroes_dict) - 1))
        print('x:{}, y:{}'.format(profile['x_pos'], profile['y_pos']))

print(heroes_dict.index(profile))
        
with Listener(on_press = on_press) as listener:
    listener.join()

