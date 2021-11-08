import colorama
import discord
from utils import configloader

currentchannel = int(open("./guildcfg", "r").read().split("\n")[1])
currentguild = open("./guildcfg", "r").read().split("\n")[0]
config = configloader.loadconfig()
valid_hex = '0123456789ABCDEF'.__contains__
prefix = config.PREFIX
user = discord.Client()
msglen = 0


def cleanhex(
        data
):  # used for cleaning the hexadecimal color codes for fore_fromhex()
    return ''.join(filter(valid_hex, data.upper()))


def fore_fromhex(text, hexcode):  # used for generating the role colors
    """print in a hex defined color"""

    if hexcode == "#000000":
        return "\033[38;2;0;0;0;48;2;255;255;255m{}".format(text)
    elif hexcode == "#FFFFFF":
        return (text, colorama.Fore.BLACK, colorama.Back.WHITE)
    hexint = int(cleanhex(hexcode), 16)
    return ("\x1B[48;2;{};{};{}m{}\x1B[0m".format(hexint >> 16,
                                                  hexint >> 8 & 0xFF,
                                                  hexint & 0xFF, text))


if config.settings.rolecolors == True:  # if rolecolors is enabled by a "1" in the cfg file colorama inits
    colorama.init()


def getcolor(user):  # gets the top role color from the user
    return str(user.top_role.color)


@user.event
async def on_ready():  # initalize the client and get the input thread running
    #inputthread = threading.Thread(target=asyncio.run(send(user)))
    # await inputthread.start()
    currentguild = int(open("guildcfg", "r").read().split("\n")[0])
    print(colorama.Fore.BLUE, "signed in as \n", user.user.display_name,
          colorama.Fore.RESET, colorama.Back.RESET)
    print(user.get_guild(currentguild).name)
    print(user.get_guild(currentguild).get_channel(currentchannel).name)


@user.event  # processing the recived messages and print them to the console
async def on_message(ctx):
    global currentchannel
    global currentguild
    if currentguild != "DM":
        currentguild = int(currentguild)
    try:
        ctx.channel.id
        ctx.guild.id
    except:
        return
    if ctx.channel.id == currentchannel:
        # await ctx.delete()
        msg = ctx.content
        print(
            ctx.guild.name + " | channel :: " + ctx.channel.name + " | " +
            fore_fromhex(ctx.author.display_name, getcolor(ctx.author)) +
            colorama.Back.RESET + colorama.Fore.RESET + " :: " + msg,
            colorama.Back.RESET, colorama.Fore.RESET)


user.run(config.TOKEN)
