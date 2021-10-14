import discord
import colorama
import asyncio
from config import config
valid_hex = '0123456789ABCDEF'.__contains__
prefix = input("please write your prefix\n>>")
class commands:
  commands = [
    "set-status",
    "set-guild",
    "set-channel"
]
def invoke(command,message):
  #preliminary check to make sure the last one didnt fuck up
  if command not in message:
    return
  if command == "set-status":

def trycommand(message):
  if message.author.id != bot.user.id:
    return
  elif message.author.id == bot.user.id:
    if prefix in message.content:
      messagecontent = (message.content).split(prefix)
      for command in commands.commands:
        if command not in message:
          continue
        elif command in message:
          invoke(command,messagecontent)
def cleanhex(data):
    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(text, hexcode):
    """print in a hex defined color"""
    if hexcode == "#000000":
      return "\033[38;2;0;0;0;48;2;255;255;255m{}".format(text)
    elif hexcode == "#FFFFFF":
      return (text,colorama.Fore.WHITE,colorama.Back.BLACK)
    hexint = int(cleanhex(hexcode), 16)
    return ("\x1B[48;2;{};{};{}m{}\x1B[0m".format(hexint>>16, hexint>>8&0xFF, hexint&0xFF, text))
bot = discord.Client()
if config.settings.rolecolors == True:
  colorama.init()
def getcolor(user):
  return str(user.top_role.color)
@bot.event
async def on_ready():
  print(colorama.Fore.BLUE,"signed in as \n",bot.user.display_name,colorama.Fore.RESET,colorama.Back.RESET)
def checkcurrentguild(currentguild,message):
  if message.guild.id == currentguild:
    return True
  elif message.guild.id != currentguild:
    return True
  else:
    return True
@bot.event
async def on_message(message):
    currentguild = 895064128052416602
    currentchannel = 895064128052416606
    if checkcurrentguild(currentguild,message):
      if message.channel.id == currentchannel:
        print(message.guild.name + " | channel :: " + message.channel.name + " | " + fore_fromhex(message.author.display_name, getcolor(message.author)) + " :: " + message.content,colorama.Back.RESET,colorama.Fore.RESET)
        if ((message.content).split("\n"))[0] == ".changeguild":
          currentguild = ((message.content).split("\n"))[1]
          currentchannel = ((message.content).split("\n"))[2]
          print(currentguild,currentchannel)
def run():
  bot.run(config.TOKEN,bot=False)
async def send(currentguild,currentchannel):
  guild = bot.get_guild(currentguild)
  for channel in bot.get_guild(currentguild).channels:
    if channel.id == currentchannel:
      await channel.send(input(">> "))
import threading
import time
run()
currentguild = 895695899706130473
currentchannel = 895695899706130476
inputthread = threading.Thread(target=asyncio.run(send(currentguild,currentchannel)))
time.sleep(1)
inputthread.start()