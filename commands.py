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
    if message== 'd':
        keyboard.press(Key.right)
    if message== 'dr':
        keyboard.release(Key.right)
        print("D Released")

    if message== 'a':
        keyboard.press(Key.left)
    if message== 'ar':
        keyboard.release(Key.left)
        print("A Released")

    if message== 's':
        keyboard.press(Key.down)
    if message== 'sr':
        keyboard.release(Key.down)
        print("S Released")

    if message== 'w':
        print("I am holding UP")
        keyboard.press(Key.up)
    if message=="wr":
        keyboard.release(Key.up)


def ARROW_Preset(message):
    if message.content == 'w':
        print(message)

def WASD_Preset(message):
    if message.content == 'w':
        print(message)