import discord
import difflib
from Data.Token import TokenDiscord
from Classes.Commands import Commands
from Classes.Reaction import Reaction
from discord.ext import command

tokenDiscord = TokenDiscord()
commands = Commands()
reaction = Reaction()
channelId = tokenDiscord.uploadToken()['idstalker']
palavras = open('Data/BadWords.txt', 'r').read().lower().split('\n')

class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="Lolzinho 😪"))
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
                elif event.content == '<3oi':
                    await event.channel.send(commands.salutation())
                elif event.content == '<3help':
                    embed = discord.Embed()
                    embed.add_field(name="<3oi", value="Saudação")
                    embed.add_field(name="<3reflexao", value="Uma reflexão para animar seu dia")
                    for key in commands.commands().keys():
                        if key != 'erro':
                            embed.add_field(name = key, value = commands.commands()[key], inline = False)
                    await event.channel.send(embed = embed)
                else:
                    await event.channel.send(commands.commands()[event.content])  
                await event.delete()
            except Exception as e:
                await event.channel.send(commands.commands()['erro'])
                print(e)

client = MyClient(Status = 'dnd')
client.run(tokenDiscord.uploadToken()['token'])