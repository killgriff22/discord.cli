from discord.ext import commands
from utils import configloader
import colorama
config = configloader.loadconfig()
prefix = config.PREFIX
currentchannel = int(open("guildcfg", "r").read().split("\n")[1])
currentguild = open("guildcfg", "r").read().split("\n")[0]
user = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)
@user.event
async def on_ready():  # initalize the client and get the input thread running
    #inputthread = threading.Thread(target=asyncio.run(send(user)))
    # await inputthread.start()
    currentguild = int(open("guildcfg", "r").read().split("\n")[0])
    print(colorama.Fore.BLUE, "signed in as \n", user.user.display_name,
          colorama.Fore.RESET, colorama.Back.RESET)
    print(user.get_guild(currentguild).name)
    print(user.get_guild(currentguild).get_channel(currentchannel).name)
@user.command(alias="cg")
async def changeguild(ctx, args):
    print("changing guild to "+user.get_guild(int(args)).name +
          ", at channel "+user.get_guild(int(args)))
    open("guildcfg", "w").write(str(user.get_guild(int(args)).id) +
                                "\n"+str(user.get_guild(int(args)).getchannel()))
    await ctx.message.delete()


# the command that will let you send special messages to the current channel (e.x. embeds)
@user.command(alias="send")
async def send(ctx, args):
    await user.get_guild(currentguild).get_channel(currentchannel).send(args)
    await ctx.message.delete()
user.run(config.TOKEN)