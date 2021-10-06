

class handler:

  def login(token):
    
  currentguild = 885038663594049576
  currentchannel = 886397752475549716
  async def sendmessage(guildid,channelid,message):
    await bot.get_guild(guildid).get_channel(channelid).send(message)
@bot.event
async def on_message(message):
  if handler.checkcurrentguild(handler.currentguild,message):
    print(message.guild.name + " : " + message.author.display_name + " : " + message.content)
#extra gay why u wanna make a cli based discord isnt the app enough lmao
#i want to use discord on my fedora server lol