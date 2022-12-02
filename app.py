import discord
import commands

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

myGuild = ""
role = ""

memberList = []

@client.event
async def on_ready():
    myGuild = client.get_guild(1047959171825405972)
    role = discord.utils.get(myGuild.roles, id=1047961554680823898)

    print(f'We have logged in as {client.user}!')  ## Prints the user name of the Bot when it connects
    print(f'Guild: {myGuild}')  # Prints the Server name where it is currently operating
    print(f'Role for sharing gameplay: {role}') # Displays the role that a viewer has to have

@client.event
async def on_message(message):
    user = message.author

    forward = False
    backwards = False
    left = False
    right = False   


    myGuild = client.get_guild(1047959171825405972)
    role = discord.utils.get(myGuild.roles, id=1047961554680823898)
    for member in role.members:
        memberList.append(member)
    
    if message.author == client.user:
        return

    if user in memberList:
        print(f'User: {user} has the role: {role}')

        
        if message.author == client.user:
            return
        if message.content.startswith('Hello'):
            await message.channel.send('Sup!')


        if message.content.startswith('Forward'):
            commands.forward(forward, backwards)
            await message.channel.send('Forward Control Toggled!')


        # Control toggling
        #if message.content.startswith('Forward'):
            #forward = True
            #if backwards == True:
                #backwards = False
                #await message.channel.send('Backwards Control Toggled OFF!')
            #await message.channel.send('Forward Control Toggled!')


        if message.content.startswith('Backwards'):
            backwards = True
            if forward == True:
                forward = False
                await message.channel.send('Forward Control Toggled OFF!')     
            await message.channel.send('Backwards Control Toggled!')

    else:
        await message.channel.send('You do not have the permission to control the game!')
        

client.run("MTA0Nzk1OTgwMjA4MjUwODg2MA.GrAq9T.Zw3XsSIcGbsvHKuJHHYLoMZYoCOfw-j8LJZNp8")

## Try getting input working in the game