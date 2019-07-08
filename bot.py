import discord
import os

TOKEN = 'NTk3ODMzOTczMzg4ODA0MDk2.XSN2VA.hly-k6Q_JZQU031l0cSwSjrTcbc'
command_call = '$'
client = discord.Client()
file = 'screen sh /home/minecraft/run.sh'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return #stolen code xd

    if message.content.startswith(command_call+'reboot'): #Command_call
        msg = 'Rebooting!'.format(message)
        await client.send_message(message.channel, msg) #Tells you its rebooting
        os.system(file)#runs the starting prompt for the server, also shutdowns bot for some reason (ISSUE IS HERE)

@client.event #also stolen
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
