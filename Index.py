from discord.ext.commands import Bot

from Token import TokenDiscord

tokenDiscord = TokenDiscord()

bot = Bot(command_prefix="<3", help_command=None)

@bot.event
async def on_ready(self):
    print(f'Logged on as {self.user}!')

bot.run(tokenDiscord.uploadToken()['token'])
