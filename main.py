from classes import *


currentguild = None
currentchannel = 604338503035256857
prefix = config.PREFIX
user = discord.Client()
msg = ""
width, height = os.get_terminal_size()
y = 0
top_bar = MultiTerm.Screen((width, 1), (0, 0))
message_space = MultiTerm.Screen((width, height-2), (0, 1))
text_bar = MultiTerm.Screen((width, 1), (0, height-1))
cluster = MultiTerm.cluster([top_bar, message_space, text_bar])
cluster.clear()
cluster.draw_all()

if config.RoleColors == True:  # if rolecolors is enabled by a "1" in the cfg file colorama inits
    colorama.init()


@user.event
async def on_ready():  # initalize the client
    cluster.draw_all()
    top_bar.blit(f"signed in as: {user.user.display_name}",
                 (0, 0), colorama.Fore.BLUE, MultiTerm.RESET)
    top_bar.draw()
    input_loop.start()


@user.event  # processing the recived messages and print them to the console
async def on_message(ctx):
    global currentchannel
    global currentguild
    global y
    if ctx.channel.id == currentchannel:
        # await ctx.delete()
        msg = ctx.content
        if y > height-2:
            y -= 1
            message_space.content.pop()
            message_space.content.append([" "]*width)
        lens = [
            len(f"{ctx.guild.name} |{ctx.channel.name} :: "),
            len(f"{ctx.author.display_name}")
        ]
        message_space.blit(f"{ctx.guild.name} | {
                           ctx.channel.name} :: ", (0, y))
        message_space.blit(f"{ctx.author.display_name}", (lens[0], y), fore_fromhex(
            getcolor(ctx.author))+MultiTerm.Fore.WHITE, MultiTerm.RESET)
        message_space.blit(f" :: {msg}", (lens[1]+lens[0], y))
        message_space.draw()
        y += 1


@tasks.loop()
async def input_loop():
    global msg
    text_bar.fill(" ")
    event = MultiTerm.window.get_event()
    if event == None:
        return
    elif type(event) == MultiTerm.asciimaticsEvent.KeyboardEvent:
        if event.key_code < 127 and event.key_code > 32:
            msg += chr(event.key_code)
        elif event.key_code == -300:
            msg = msg[:-1]
        elif event.key_code == 10:
            channel = user.get_channel(currentchannel)
            await channel.send(msg)
            msg = ""
        elif event.key_code == 32:
            msg += " "
        elif event.key_code == -1:
            pass
        else:
            msg += str(event.key_code)
    text_bar.blit(f"{prefix} {msg}", (0, 0))
    text_bar.draw()
user.run(config.TOKEN)
