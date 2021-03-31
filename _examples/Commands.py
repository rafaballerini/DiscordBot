from discord.ext import commands

from datetime import datetime


class Commands(commands.Cog):
    @commands.command(name="reflexao")
    async def reflexao_command(self, ctx):
        await ctx.send(
            '''Já é outro dia e você ainda está com o mesmo problema? Está desnimado, cansado pensando em largar tudo e vender coco na praia?
Lembre-se do caminho que trilhou até chegar aqui e quantos problemas já venceu..
O problema que está passando é só mais um degrau, e depende de você utrapassa-lo ou evitá-lo.
Força!! :muscle::wink: ''')

    @commands.command(name="jairo")
    async def jairo_command(self, ctx):
        timeNow = datetime.now()

        message = " só pros meu fãs e pra mulherada"

        if timeNow.hour < 12 and timeNow.hour >= 6:
            message = "Bom dia" + message
        elif timeNow.hour >= 12 and timeNow.hour < 19:
            message = "Boa tarde" + message
        else:
            message = "Boa noite" + message

        await ctx.send(message)

    @commands.command(name="rafa")
    async def rafa_command(self, ctx):
        await ctx.send("oh disus")

    @commands.command(name="matan")
    async def matan_command(self, ctx):
        await ctx.send("Pergunte-me o que quiser, que eu te darei a resposta")

    @commands.command(name="arthur")
    async def arthur_command(self, ctx):
        await ctx.send("Vou comer vidro e chorar no banho dps dessa....:smiling_face_with_tear:")

    @commands.command(name="ander")
    async def ander_command(self, ctx):
        await ctx.send("Boa cxr, ce merece")

    @commands.command(name="kyle")
    async def kyle_command(self, ctx):
        await ctx.send("E vamos pro off topic , esse chat ficou totalmente desvirtuado")

    @commands.command(name="agua")
    async def agua_command(self, ctx):
        await ctx.send("--> Bebam Água <--")

    @commands.command(name="joelzin")
    async def joelzin_command(self, ctx):
        await ctx.send("https://tenor.com/view/tohru-dragonmaid-anime-gif-9656401")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.error.CommandNotFound):
            await ctx.send("Esse comando não existe! :alien:")
        else:
            raise error


def setup(bot):
    cog = Commands()
    bot.add_cog(cog)
