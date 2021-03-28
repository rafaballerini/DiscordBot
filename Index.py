import discord
from Token import TokenDiscord
from Commands import Commands

tokenDiscord = TokenDiscord()
commands = Commands()

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
                else:
                    await message.channel.send(commands.commands()[message.content])  
            except:
                await message.channel.send(commands.commands()['erro'])

client = MyClient()
client.run(tokenDiscord.uploadToken()['token'])