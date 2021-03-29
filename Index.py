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

client = MyClient()
client.run(tokenDiscord.uploadToken()['token'])