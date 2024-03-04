from classes import *

if open("./guildcfg", "r").read() != "":
    currentchannel = int(open("./guildcfg", "r").read().split("\n")[1])
    currentguild = int(open("./guildcfg", "r").read().split("\n")[0])
prefix = config.PREFIX
user = discord.Client()
msglen = 0
width,height = os.get_terminal_size()

top_bar = MultiTerm.Screen((width,1),(0,0))
message_space = MultiTerm.Screen((width,height-2),(0,1))
text_bar = MultiTerm.Screen((width,1),(0,height-1))

if config.RoleColors == True:  # if rolecolors is enabled by a "1" in the cfg file colorama inits
    colorama.init()




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
