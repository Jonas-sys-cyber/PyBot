import discord
from discord.ext import commands
import random
import asyncio



page ="https://www.google.de/search?q= "

bot = commands.Bot(command_prefix="")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("bot is now online")

answers = ["Yes", "No", "Maybe", "maybe not", "Probably", "Probably not"]


@bot.command(pass_context=True)
async def help(ctx):
    await ctx.send("Help\r\n"
                   "?help - shows all commands\r\n"
                   "?hello - greeats you")

@bot.command(pass_context=True)
async def hallo(ctx):
    await ctx.send(f"Hey {ctx.message.author.name}!")

@bot.command(pass_context=True)
async def tschüss(ctx):
    await ctx.send("bye")

@bot.command(pass_context=True)
async def hi(ctx):
    await ctx.send(f"Moin {ctx.message.author.name}!")

@bot.command(pass_context=True)
async def sage(ctx,arg):
    await ctx.send(arg)

@bot.command(pass_context=True)
async def apple(ctx):
    await ctx.send(f"Apple ist scheiße {ctx.message.author.name}!")

@bot.command(pass_context=True)
async def google(ctx,arg):
    url = page.replace(" ",str(arg))
    await ctx.send(url)

@bot.command(pass_context=True)
async def moin(ctx,arg):
    await ctx.send("hi")

@bot.command(pass_context=True)
async def schreibe(ctx,arg):
    await ctx.send(arg)


@bot.command(pass_context=True)
async def bye(ctx):
    await ctx.send(f"Tschüss {ctx.message.author.name}!")

@bot.command(pass_context=True)
async def hilfe(ctx,arg):
    await ctx.send(f"Frage einen Admin {ctx.message.author.name}!")
    
@bot.command(pass_context=True)
async def cool(ctx):
    await ctx.send(f"ziemlich nice{ctx.message.author.name}!")

@bot.command(pass_context=True)
async def nice(ctx):
    await ctx.send(f"find ich auch{ctx.message.author.name}!")

@bot.command(pass_context=True)
async def lulrank(ctx):
    await ctx.send(f"Wie findest du deinen Rank {ctx.message.author.name}?")

@bot.command(pass_context=True)
async def gut(ctx):
    await ctx.send(f"schön{ctx.message.author.name}.")

@bot.command(pass_context=True)
async def schlecht(ctx):
    await ctx.send(f"tut mir leid{ctx.message.author.name}.")

@bot.command(pass_context=True)
async def luldaily(ctx):
    await ctx.send(f"Was hast du vor{ctx.message.author.name}?")

@bot.command(pass_context=True)
async def avertar(ctx):
    await ctx.send(f"Was hast du vor{ctx.message.author.name}? Du hast das F! vergessen")

@bot.command(pass_context=True)
async def MEE6(ctx):
    await ctx.send(f"Warum schreibst du mit einem anderem Bot{ctx.message.author.name}?! ")

@bot.command(pass_context=True)
async def Groovy(ctx):
    await ctx.send(f"Warum schreibst du mit einem anderem Bot{ctx.message.author.name}?! ")











bot.run("ODA4MzgzMjQ2NjU5NjE2ODA5.YCFvkQ.kLwtiFIKc2NT8X0Md6Eg2-kAtDU")
