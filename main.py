import os
import discord
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

prefix = "ZabidDevelopment - "
token = os.environ['TOKEN']
bot = commands.Bot(command_prefix=".")
welcome_channel = 985720805327532142

# Help Command
@bot.command()
async def zhelp(ctx):
  embed=discord.Embed(title="List of Commands", color=0xb903dd)
  embed.add_field(name="Tutorials", value="`.indention` `.yaml` `.websockets` `.conditions` `.lists` `.scoreboard` `.commands` `.functions` `.packets`", inline=True)
  embed.set_footer(text="Zabrid Development- Help")
  await ctx.send(embed=embed)

# Indention Tutorial
# https://skripthub.net/tutorials/33
@bot.command()
async def indention(ctx):
  embed=discord.Embed(title="Indention Tutorial (Click Here)", url="https://skripthub.net/tutorials/33", description="Click the link above for a tutorial on skript indention.", color=0xb903dd)
  embed.set_author(name="Charcoal Toast", url="https://forums.skunity.com/members/charcoaltoast.6140/", icon_url="https://forums.skunity.com/data/avatars/l/6/6140.jpg?1551464651")
  embed.set_footer(text="SkriptHub Tutorial #33")
  await ctx.send(embed=embed)

# Packets Tutorial 
# https://skripthub.net/tutorials/2
@bot.command()
async def packets(ctx):
  embed=discord.Embed(title="Packets Tutorial (Click Here)", url="https://skripthub.net/tutorials/26", description="Click the link above for a tutorial on skript packets.", color=0xb903dd)
  embed.set_author(name="Tlatoani", url="https://forums.skunity.com/members/minecoll_yt.7188/", icon_url="https://forums.skunity.com/data/avatars/l/7/7188.jpg?1621084875")
  embed.set_footer(text="SkriptHub Tutorial #26")
  await ctx.send(embed=embed)

# Websockets Tutorial
# https://skripthub.net/tutorials/7
@bot.command()
async def websockets(ctx):
  embed=discord.Embed(title="Websockets Tutorial (Click Here)", url="https://skripthub.net/tutorials/7", description="Click the link above for a tutorial on skript websockets.", color=0xb903dd)
  embed.set_author(name="Tlatoani", url="https://forums.skunity.com/members/minecoll_yt.7188/", icon_url="https://forums.skunity.com/data/avatars/l/7/7188.jpg?1621084875")
  embed.set_footer(text="SkriptHub Tutorial #7")
  await ctx.send(embed=embed)

# Functions Tutorial
# https://skripthub.net/tutorials/9
@bot.command()
async def functions(ctx):
  embed=discord.Embed(title="Functions Tutorial (Click Here)", url="https://skripthub.net/tutorials/9", description="Click the link above for a tutorial on skript functions.", color=0xb903dd)
  embed.set_author(name="Blueyescat", url="https://forums.skunity.com/members/blueyescat.127/", icon_url="https://secure.gravatar.com/avatar/8dd840112336b930de0692fbbd683a02?s=192&d=https%3A%2F%2Fforums.skunity.com%2Fstyles%2Fuix%2Fxenforo%2Favatars%2Favatar_male_l.png")
  embed.set_footer(text="SkriptHub Tutorial #9")
  await ctx.send(embed=embed)

# Commands Tutorial
# https://skripthub.net/tutorials/10
@bot.command()
async def commands(ctx):
  embed=discord.Embed(title="Commands Tutorial (Click Here)", url="https://skripthub.net/tutorials/10", description="Click the link above for a tutorial on skript commands.", color=0xb903dd)
  embed.set_author(name="Blueyescat", url="https://forums.skunity.com/members/blueyescat.127/", icon_url="https://secure.gravatar.com/avatar/8dd840112336b930de0692fbbd683a02?s=192&d=https%3A%2F%2Fforums.skunity.com%2Fstyles%2Fuix%2Fxenforo%2Favatars%2Favatar_male_l.png")
  embed.set_footer(text="SkriptHub Tutorial #10")
  await ctx.send(embed=embed)

# YAML Tutorial
# https://skripthub.net/tutorials/25
@bot.command()
async def yaml(ctx):
  embed=discord.Embed(title="YAML Tutorial (Click Here)", url="https://skripthub.net/tutorials/25", description="Click the link above for a tutorial on skript-yaml.", color=0xb903dd)
  embed.set_author(name="Olyno", url="https://forums.skunity.com/members/olyno.823/", icon_url="https://secure.gravatar.com/avatar/e9d1a35bfad444c9f0a73b9cbc62469c?s=192&d=https%3A%2F%2Fforums.skunity.com%2Fstyles%2Fuix%2Fxenforo%2Favatars%2Favatar_male_l.png")
  embed.set_footer(text="SkriptHub Tutorial #25")
  await ctx.send(embed=embed)


# Lists Tutorial 
# https://skripthub.net/tutorials/2
@bot.command()
async def lists(ctx):
  embed=discord.Embed(title="List Tutorial (Click Here)", url="https://skripthub.net/tutorials/31", description="Click the link above for a tutorial on skript list variables.", color=0xb903dd)
  embed.set_author(name="Goose", url="https://forums.skunity.com/members/goose.9345/", icon_url="https://forums.skunity.com/data/avatars/l/9/9345.jpg?1608703880")
  embed.set_footer(text="SkriptHub Tutorial #31")
  await ctx.send(embed=embed)


# Conditions Tutorial 
# https://skripthub.net/tutorials/2
@bot.command()
async def conditions(ctx):
  embed=discord.Embed(title="Conditions Tutorial (Click Here)", url="https://skripthub.net/tutorials/35", description="Click the link above for a tutorial on skript conditions.", color=0xb903dd)
  embed.set_author(name="BluBoy3ch0", icon_url="https://imgs.search.brave.com/hsGWQck_QG4GpDOog9JJajDZkHQwgMQq4gIWL149tbU/rs:fit:900:900:1/g:ce/aHR0cHM6Ly95dDMu/Z2dwaHQuY29tL2Ev/QUFUWEFKejltaFFn/MFRlYTY1cGtMekEw/eTRodF85bVExZ3Bj/OVlEUzhRPXM5MDAt/Yy1rLWMweGZmZmZm/ZmZmLW5vLXJqLW1v")
  embed.set_footer(text="SkriptHub Tutorial #35")
  await ctx.send(embed=embed)

# Scoreboard Tutorial 
# https://skripthub.net/tutorials/2
@bot.command()
async def scoreboard(ctx):
  embed=discord.Embed(title="Scoreboard Tutorial (Click Here)", url="https://skripthub.net/tutorials/50", description="Click the link above for a tutorial on skript list variables.", color=0xb903dd)
  embed.set_author(name="JakeTheChad", url="https://forums.skunity.com/members/jakethechad.21267/", icon_url="https://forums.skunity.com/data/avatars/l/21/21267.jpg?1649950824")
  embed.add_field(name="ZScoreboard", value="Or, instead of learning to code you could use ZScoreboard https://forums.skunity.com/resources/zscoreboard.1422/", inline=False)
  embed.set_footer(text="SkriptHub Tutorial #50")
  await ctx.send(embed=embed)


# Expressions Tutorial 
# https://skripthub.net/tutorials/51
@bot.command()
async def expressions(ctx):
  embed=discord.Embed(title="Custom Expressions Tutorial (Click Here)", url="https://skripthub.net/tutorials/51", description="Click the link above for a tutorial on custom skript expressions.", color=0xb903dd)
  embed.set_author(name="average", icon_url="https://imgs.search.brave.com/hsGWQck_QG4GpDOog9JJajDZkHQwgMQq4gIWL149tbU/rs:fit:900:900:1/g:ce/aHR0cHM6Ly95dDMu/Z2dwaHQuY29tL2Ev/QUFUWEFKejltaFFn/MFRlYTY1cGtMekEw/eTRodF85bVExZ3Bj/OVlEUzhRPXM5MDAt/Yy1rLWMweGZmZmZm/ZmZmLW5vLXJqLW1v")
  embed.set_footer(text="SkriptHub Tutorial #51")
  await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
  await bot.get_channel(985720805327532142).send(member.name + "has joined")
  print("worked!")
  #embed=discord.Embed(title="Welcome to the server " + format(user), color=0xb903dd)
  
  
# On ready print message to console
@bot.event
async def on_ready():
  print('------')
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')
  

keep_alive()
bot.run(token)