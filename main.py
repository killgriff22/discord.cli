from functions import *

cluster.clear()
cluster.draw_all()
if config.RoleColors == True:  # if rolecolors is enabled by a "1" in the cfg file colorama inits
    colorama.init()


@user.event
async def on_ready():  # initalize the client
    global mode
    mode=modes.messages
    cluster.draw_all()
    top_bar.blit(f"signed in as: {user.user.display_name}, guild: {user.get_guild(currentguild).name}, channel: {user.get_channel(currentchannel).name}",
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
        message_space.blit(f"{ctx.guild.name} | {ctx.channel.name} :: ", (0, y))
        message_space.blit(f"{ctx.author.display_name}", (lens[0], y), fore_fromhex(
            getcolor(ctx.author))+MultiTerm.Fore.WHITE, MultiTerm.RESET)
        message_space.blit(f" :: {msg}", (lens[1]+lens[0], y))
        if mode == modes.messages:
            message_space.draw()
        y += 1


@tasks.loop()
async def input_loop():
    global msg, mode,channel_index,currentchannel,currentguild
    if mode == modes.exit:
        user.close()
        exit()
    text_bar.fill(" ")
    event = MultiTerm.window.get_event()
    if event == None:
        return
    elif type(event) == MultiTerm.asciimaticsEvent.KeyboardEvent:
        if mode == modes.messages:
            if event.key_code < 127 and event.key_code > 32:
                msg += chr(event.key_code)
            elif event.key_code == -300:
                msg = msg[:-1]
            elif event.key_code == 10:
                output,mode = process_command(msg)
                if not output:
                    channel = user.get_channel(currentchannel)
                    await channel.send(msg)
                msg = ""
            elif event.key_code == 32:
                msg += " "
            elif event.key_code == -1:
                pass
            else:
                msg += str(event.key_code)
        elif mode == modes.channels:
            channel_list = user.get_guild(currentguild).channels
            if event.key_code == 10:
                mode = modes.messages
                msg = ""
                currentchannel = channel_list[channel_index].id
                selection_box.clear()
                message_space.draw()
            for i,channel in enumerate(channel_list):
                selection_box.blit(channel.name, (0, i),
                                    MultiTerm.Fore.BLACK+MultiTerm.Back.WHITE if i == channel_index else \
                                        MultiTerm.Fore.WHITE+MultiTerm.Back.BLACK,MultiTerm.RESET)
            msg = str(channel_index)
            selection_box.draw()
            key = process_arrows(event)
            if key == "up":
                channel_index -= 1
                if channel_index < 0:
                    channel_index = len(channel_list)-1
            elif key == "down":
                channel_index += 1
                if channel_index >= len(channel_list):
                    channel_index = 0
        else:
            if event.key_code == 10:
                mode = modes.messages
    text_bar.blit(f"{prefix} {msg}", (0, 0))
    text_bar.draw()
    top_bar.blit(f"signed in as: {user.user.display_name}, guild: {user.get_guild(currentguild).name}, channel: {user.get_channel(currentchannel).name}",(0,0))
    top_bar.draw()
    cursor_pos(0,height-1)
user.run(config.TOKEN)
