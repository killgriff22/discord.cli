import discord
import colorama
import asyncio
from config import config
currentguild = 885038663594049576
currentchannel = 886397752475549716
bot = discord.Client()
def checkcurrentguild(currentguild,message):
  if message.guild.id == currentguild:
    return True
  elif message.guild.id != currentguild:
    return False
  else:
    return False 
currentguild = 885038663594049576
currentchannel = 886397752475549716
@bot.event
async def on_message(message):
  #if message.content[0] == ".":
  #if message.content == ".changeguild":
    #msg = message.content.split(" ")
    #currentguild = int(msg[1])
  #else:
    #if checkcurrentguild(currentguild,message.guild.id):
      #if message.channel.id == currentchannel:
        print(message.guild.name + " | channel :: " + message.channel.name + " | " + message.author.display_name + " :: " + message.content)
bot.run(config.TOKEN,bot=False)