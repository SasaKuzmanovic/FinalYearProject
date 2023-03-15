# Viewer playing commands
from pynput.keyboard import Key, Controller

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
        keyboard.release(Key.left)
        keyboard.press(Key.right)
    if message.content == 'a':
        keyboard.release(Key.right)
        keyboard.press(Key.left)
        print(message.content)
    if message.content == 'b':
        keyboard.release(Key.left)
    if message.content == 'w':
        print(message.content)
        keyboard.release(Key.up)
        keyboard.press(Key.up)