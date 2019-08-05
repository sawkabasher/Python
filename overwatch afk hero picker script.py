import time 
import threading
import keyboard
from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Button, Controller
import pyttsx3
from gtts import gTTS
import playsound
import os.path

profiles = profiles = (('widowmaker',1410,910),
                       ('sombra',1177,910),
                       ('tracer',1350,910),
                        ('mercy',1716,910),
                        ('ana',1486,910),
                       ('mccree',884,910),
                        ('genji',712,910),
                       ('wrecking ball',402,910),
                       ('zArya',460,910))
profile = profiles[0]

start_stop_key = Key.f2
switch_profile_key = Key.f4
exit_key = Key.f12

if os.path.exists('sounds'):
    pass
else:
    os.mkdir('sounds')
    tts = gTTS(text="press F4 to switch between profiles and press F2 to start", lang="en")
    tts.save('sounds\welcome.mp3')
    tts = gTTS(text="start", lang="en")
    tts.save('sounds\start.mp3')
    tts = gTTS(text="stop", lang="en")
    tts.save('sounds\stop.mp3')

    for row in profiles:
        tts = gTTS(text=row[0], lang="en")
        tts.save('sounds\{}.mp3'.format(row[0]))




mouse = Controller()

class Main(threading.Thread):
    
    def __init__(self):
        print('press F4 to switch between profiles and press F2 to start')
        print (profile)

        playsound.playsound('sounds\welcome.mp3', False)
        time.sleep(4)
        playsound.playsound('sounds\{}.mp3'.format(profile[0]),False)
        
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
                mouse.position = (profile[1],profile[2])
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
        
    
    elif key == switch_profile_key:
        
        if profiles.index(profile) < (len(profiles) - 1):
            profile = profiles[profiles.index(profile) + 1]
        else:
            profile = profiles[0]
        playsound.playsound('sounds\{}.mp3'.format(profile[0]), False)
        print('{}/{}'.format(profiles.index(profile), len(profiles) - 1))
        print('x:{}, y:{}'.format(profile[1], profile[2]))

    elif key == exit_key:
        main_thread.exit5listener.stop()
        
with Listener(on_press = on_press) as listener:
    listener.join()

