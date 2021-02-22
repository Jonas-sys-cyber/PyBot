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

answers = ["ja", "nein", "vielleicht ", "vieleicht nicht", "warscheinlich", "warscheinlich nicht"]


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
    await ctx.send(f"Was hast du vor {ctx.message.author.name}?")


@bot.command(pass_context=True)
async def MEE6(ctx):
    await ctx.send(f"Warum schreibst du mit einem anderem Bot{ctx.message.author.name}?! ")

@bot.command(pass_context=True)
async def Groovy(ctx):
    await ctx.send(f"Warum schreibst du mit einem anderem Bot{ctx.message.author.name}?! ")


@bot.command(pass_context=True)
async def FlashBot(ctx):
    await ctx.send("F!... ")

@bot.command(pass_context=True)
async def lulhelp(ctx):
    await ctx.send("lul... ")

@bot.command(pass_context=True)
async def Lulrank(ctx):
    await ctx.send(f"Wie findest du deinen Rank {ctx.message.author.name}?")

@bot.command(pass_context=True)
async def Lultop(ctx):
    await ctx.send(f"Wie ist dein Level den ?")

@bot.command(pass_context=True)
async def Ja(ctx):
    await ctx.send(f"ich stimme dir zu {ctx.message.author.name}")

@bot.command(pass_context=True)
async def nein(ctx):
    await ctx.send(f"ich stimme dir zu {ctx.message.author.name}")

@bot.command(pass_context=True)
async def spam(ctx,arg):
    while 1:
        await ctx.send(arg)
        

@bot.command(pass_context=True)
async def Apple (ctx):
    await ctx.send(f"Ich hasse Apple weil es Scheisse Teuer ist und nichts kann,falls du Appel magst hasse ich dich {ctx.message.author.name}?")

@bot.command(pass_context=True)
async def apple (ctx):
    await ctx.send(f"Ich hasse Apple weil es Scheisse Teuer ist und nichts kann,falls du Appel magst hasse ich dich {ctx.message.author.name}?")

@bot.command(pass_context=True)
async def lulrank (ctx):
    await ctx.send(f"Wie fibndest du deinen Rank {ctx.message.author.name} ?"

@bot.command(pass_context=True)
async def lultop (ctx):
    await ctx.send(f"Du bist doch bestimmt SCHEISSE {ctx.message.author.name} ?"

@bot.command(pass_context=True)
async def lulhack (ctx):
    await ctx.send(f"Wen willst du denn Hacken {ctx.message.author.name} ?"

@bot.command(pass_context=True)
async def lulsearch (ctx):
    await ctx.send(f"Was suchst du {ctx.message.author.name} ?"

@bot.command(pass_context=True)
async def google(ctx,arg):
    url = page.replace(" ",str(arg))
    await ctx.send(url)






bot.run("ODA4MzgzMjQ2NjU5NjE2ODA5.YCFvkQ.tKFjl0ddGFNoSAjGQ4cymj9eWkw")
