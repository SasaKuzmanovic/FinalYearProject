import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

forward = False
backwards = False
left = False
right = False

myGuild = ""
role = ""

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}!')
    myGuild = client.get_guild(1047959171825405972)
    print(f'Guild: {myGuild}')
    role = discord.utils.get(myGuild.roles, id=1047961554680823898)
    print(f'Role: {role}')


@client.event
async def on_message(message):
    user = message.author
    memberList = []
    memberList = discord.Role.members
    #print(f'User: {user}')
    #print(user.roles)
    #if role in user.roles:
    #print(f'I have the role {role}')    
    if message.author == client.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send('Sup!')
    
    # Control toggling
    if message.content.startswith('Forward'):
        forward = True
        backwards = False
        await message.channel.send('Forward Control Toggled')
    if message.content.startswith('Backwards'):
        backwards = True
        forward = False
        message.channel.send('Hello')
        await message.channel.send('Backwards Control Toggled')
    #else:
        #await message.channel.send('You do not have the permission to control the game!')
client.run("MTA0Nzk1OTgwMjA4MjUwODg2MA.GrAq9T.Zw3XsSIcGbsvHKuJHHYLoMZYoCOfw-j8LJZNp8")