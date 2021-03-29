import discord
from Token import TokenDiscord
from Commands import Commands
from datetime import datetime

tokenDiscord = TokenDiscord()
commands = Commands()
timeNow = datetime.now()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #channelId=tokenDiscord.uploadToken()['idstalker']
        if message.author.bot:
            return

        # for palavra in palavras.split(palavras, ','):
        #     if message.content.find(palavra) != -1 :
        #         #await message.delete()
        #         print(f'deletar mensagem {message.content}')

        #channel = self.get_channel(channelId)
        #await channel.send(f'Canal {message.channel.mention} enviada por {message.author.mention}: {message.content}')

        if message.content.startswith('<3'):
            try:
                if message.content == '<3reflexao':
                    await message.channel.send(commands.reflection()) 
                elif message.content == '<3jairo':
                    if timeNow.hour < 12 and timeNow.hour >= 6:
                        await message.channel.send(commands.morning())
                    elif timeNow.hour >= 12 and timeNow.hour < 19:
                        await message.channel.send(commands.afternoon())
                    else:
                        await message.channel.send(commands.night())   
                else:
                    await message.channel.send(commands.commands()[message.content])  
            except:
                await message.channel.send(commands.commands()['erro'])

client = MyClient()
client.run(tokenDiscord.uploadToken()['token'])