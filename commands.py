# Viewer playing commands
from pynput.keyboard import Key, Controller

import time

keyboard = Controller()

def forward():
    forward = True
    backwards = False

def backwards():
    forward = False
    backwards = True

def checkForContents(message):
    if message.content == 'd':
        print(message.content)
        keyboard.press(Key.right)
    if message.content == 'a':
        keyboard.press(Key.left)
        print(message.content)
    if message.content == 's':
        keyboard.release(Key.left)
        keyboard.press(Key.down)
        keyboard.release(Key.left)
    if message.content == 'w':
        print("I am holding UP")

        #keyboard.release(Key.up)
        keyboard.press(Key.up)


def ARROW_Preset(message):
    if message.content == 'w':
        print(message.content)

def WASD_Preset(message):
    if message.content == 'w':
        print(message.content)