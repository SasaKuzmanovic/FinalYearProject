# Button Presets
import time
from pynput.keyboard import Key, Controller

def controlIntro():
    time.sleep(0.5)

    print('====================================')
    print('======Please select the preset======')

    time.sleep(0.5)

    print('====================================')
    print('==To select a preset type its name==')

    time.sleep(0.2)

    print('====================================')
    print('==============PRESETS===============')
    print('==============1. WASD===============')

    time.sleep(0.1)
    
    print('==============2. ARROWS=============')

    print('Example: WASD')

    newInput = input()

    time.sleep(0.3)


    if newInput == 'WASD':
        print('====================================')
        print('=========You selected: WASD=========')
    
    if newInput == 'ARROWS':
        print('====================================')
        print('========You selected: Arrows========')

    if newInput != "WASD" and newInput != "ARROWS":
        print('====================================')
        print('=====ERROR: No such preset found====')
    
    return newInput
    
