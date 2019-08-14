import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')
makar_photos = ('https://sun9-53.userapi.com/c845418/v845418981/4a82d/9ARWYICWmqY.jpg',
                'https://sun9-28.userapi.com/c846524/v846524490/1fb130/ZkUaH0vyBkg.jpg',
                'https://pp.userapi.com/c844521/v844521639/16bb75/oKhj0FytBFY.jpg',
                'https://sun9-7.userapi.com/c848624/v848624963/730a4/Hyfj52_yXeQ.jpg',
                'https://sun9-27.userapi.com/c841623/v841623573/1f6d6/BsS34kytuno.jpg',
                'https://sun9-54.userapi.com/c824600/v824600863/5dcfb/pzfX8y5ivc8.jpg',
                'https://sun9-49.userapi.com/c841323/v841323668/3cfbe/F_AZSeeiwcc.jpg',
                'https://pp.userapi.com/c836639/v836639481/3fd7b/prtzxG6Q8iY.jpg',
                'https://pp.userapi.com/c637219/v637219481/4c361/8GLrirt0y98.jpg',
                'https://sun9-13.userapi.com/c837423/v837423481/47023/ISTkSkdPQro.jpg',
                'https://sun9-1.userapi.com/c638426/v638426481/add3/LavhVFfxrV8.jpg',
                'https://sun9-38.userapi.com/c837634/v837634481/1bd21/53DoAqeBRdA.jpg',
                'https://sun9-18.userapi.com/c637318/v637318481/27919/1X3j6PzJHXY.jpg',
                'https://sun9-32.userapi.com/c626831/v626831481/1d1a4/cqb9VCuJ8XE.jpg',
                'https://sun9-52.userapi.com/c629216/v629216481/3738f/zZSaLrwXFFU.jpg',
                'https://sun9-44.userapi.com/c629401/v629401481/1683b/GFrMB_pEd4w.jpg',
                'https://pp.userapi.com/c628225/v628225481/20704/13L8-xTWA8E.jpg',
                'https://sun9-49.userapi.com/c623725/v623725481/46023/YdGO2KlU744.jpg',
                'https://sun9-14.userapi.com/c623724/v623724481/4725c/re-VDGT2EUs.jpg',
                'https://sun9-21.userapi.com/c629231/v629231481/3389/7jtkwpm4HGM.jpg')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def hi(ctx):
    await ctx.send(":gay_pride_flag: :gay_pride_flag: :gay_pride_flag: :wave: Hello, there!")

@bot.command()
async def makar(ctx):
    await ctx.send(random.choice(makar_photos))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    embed.add_field(name="Author", value="sashka")
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="MAKAP-76", value="47)))0000")

    await ctx.send(embed=embed)

bot.remove_command('help')
bot.remove_command('info')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="A Very Nice bot. List of commands are:", description=" ", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$hi", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$makar", value="Gives dick pic.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NjExMTY4NDUwMjc4MDY0MTQ3.XVP6JA.Cvrzi-JL-qFDf4Df47K9xK7BQWI')
