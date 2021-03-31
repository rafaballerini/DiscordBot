import discord
import difflib
from Data.Token import TokenDiscord
from Classes.Commands import Commands
from Classes.Reaction import Reaction

tokenDiscord = TokenDiscord()
commands = Commands()
reaction = Reaction()
channelId = tokenDiscord.uploadToken()['idstalker']
palavras = open('Data/BadWords.txt', 'r').read().lower().split('\n')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_raw_reaction_add(self, event):
        reaction.channel_reaction(event)

    async def on_message(self, event):
        event.content = event.content.lower()
        if event.author.bot:
            return

        for mensagem in event.content.split():
            if mensagem in palavras:
                if event.content.find('gado') != -1 or event.content.find('gados') != -1:
                    await event.channel.send(f'{event.author.mention} falou: {event.content.replace("gados", "gostosos").replace("gado", "gostoso")}')
                await event.delete()

        #channel = self.get_channel(channelId)
        #await channel.send(f'Canal {event.channel.mention} enviada por {event.author.mention}: {event.content}')

        if event.content.startswith('<3'):
            try:
                if event.content == '<3reflexao':
                    await event.channel.send(commands.reflection()) 
                elif event.content == '<3jairo':
                    await event.channel.send(commands.salutation())
                else:
                    await event.channel.send(commands.commands()[event.content])  
                await event.delete()
            except:
                await event.channel.send(commands.commands()['erro'])

client = MyClient()
client.run(tokenDiscord.uploadToken()['token'])