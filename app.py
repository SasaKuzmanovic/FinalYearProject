import discord
import commands
import button_presets
import pygame
import time
import socket


from pynput.keyboard import Key, Controller

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP = "109.76.62.13"
TCP_IP = ""
PORT = 9011
buffer_size = 1024
msg = ("X PRESSED...")

buttonToBePressed = ""

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

myGuild = ""
role = ""

saveChannel = ""

joysticks = {}
keyboard = Controller()

memberList = []

@client.event
async def on_ready():
    pygame.init()

    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        print(f'Initan sam') 

    button_presets.controlIntro()

    print(f'Choose if you are a streamer or a viewer!')
    print(f'Select [1] if you are a streamer')
    print(f'Or select [2] if you are a viewer')

    value = input('Type 1 or 2:')

    if value == '2':
        print('====================================')
        print('========You are now a viewer========')
        print('====================================')
        print('=======Say "Hello" to the bot=======')
        print('========To play, say "Play"=========')
        print('====================================')
    else:
        myGuild = client.get_guild(1047959171825405972)
        role = discord.utils.get(myGuild.roles, id=1047961554680823898)
        print('====================================')
        print('=========Streamer Selected==========')
        print('====================================')
        print('Enjoy shared gameplay')
        waitForInput()
        

def sendInput(button):
    print("Attempting to send message: " + button)
    sock.send(button.encode('utf8'))

    data = sock.recv(buffer_size).decode('utf-8')
    print("Received: " + data)


def waitForInput():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_ip = ""
    port = 9011
    s.bind((tcp_ip, port))
    s.listen(1)

    con, addr = s.accept()
    print("Connection from: ", addr)
    while True:
        data = con.recv(buffer_size).decode('utf-8')
        if not data:
            break
        print("Data received: " + data)
        buttonToBePressed = data
        commands.checkForContents(buttonToBePressed)
        con.send(data.encode('utf-8'))
    s.close()
    

def waitingForInput():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0: ## This is X
                    # To be added   1. Add message sending to channels
                    #               2. Triggering a function when a button is pressed and the message is sent to discord. Try to trigger the function before the message is sent to reduce latency
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")
                    sendInput('w')
                if event.button == 1:
                    sendInput('s')
                if event.button == 13:
                    sendInput('a')
                if event.button == 14:
                    sendInput('d')

            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    sendInput('wr')
                if event.button == 13:
                    sendInput('ar')
                if event.button == 14:
                    sendInput('dr')

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")


@client.event
async def on_message(message):
    user = message.author

    forward = False
    backwards = False
    left = False
    right = False   
    saveChannel = message.channel

    myGuild = client.get_guild(1047959171825405972)
    role = discord.utils.get(myGuild.roles, id=1047961554680823898)
    for member in role.members:
        memberList.append(member)
    
    if message.author == client.user:
        return

    if user in memberList:
        print(f'User: {user} has the role: {role}')

        print(message.content)
        commands.checkForContents(message)

        if message.author == client.user:
            return
        if message.content.startswith('Hello'):
            await message.channel.send('Sup!')


        if message.content.startswith('Play'):
            await message.channel.send('You are now allowed to play!')
            sock.connect((SERVER_IP, PORT))
            waitingForInput()
    else:
        await message.channel.send('You do not have the permission to control the game!')
        
client.run("MTA0Nzk1OTgwMjA4MjUwODg2MA.G5XCLt.ZOodFHcrD54e8oWgtuhjNejRUWeFBEeQHR0z2w")