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
        keyboard.press(Key.right)
    if message.content == 'a':
        print(message.content)
        keyboard.press(Key.left)
    if message.content == 'space':
        print(message.content)
        keyboard.press(Key.space)
