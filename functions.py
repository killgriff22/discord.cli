from classes import *


def getcolor(user):  # gets the top role color from the user
    return str(user.top_role.color)

def cleanhex(data):  # used for cleaning the hexadecimal color codes for fore_fromhex()
    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(hexcode):  # used for generating the role colors
    """print in a hex defined color"""

    if hexcode == "#000000":
        return "\033[38;2;0;0;0;48;2;255;255;255m"
    elif hexcode == "#FFFFFF":
        return colorama.Fore.BLACK+colorama.Back.WHITE
    hexint = int(cleanhex(hexcode), 16)
    return ("\x1B[48;2;{};{};{}m".format(hexint >> 16,
                                         hexint >> 8 & 0xFF,
                                         hexint & 0xFF))


def cursor_pos(x, y):  # used for moving the cursor
    print(f"\033[{y};{x}H", end="")


def process_command(msg):
    global channel_index
    command = msg.split(" ")
    match command.pop(0):
        case "exit":
            return True, modes.exit
        case "help":
            return True, modes.command_seeker
        case "channel":
            channel_index = 0
            return True, modes.channels
        case "":
            pass
        case _:
            return False, modes.messages
    return False, False, ""


def process_arrows(event):
    if event.key_code == -204:
        return "up"
    elif event.key_code == -206:
        return "down"
    elif event.key_code == -203:
        return "left"
    elif event.key_code == -205:
        return "right"
    else:
        return False
