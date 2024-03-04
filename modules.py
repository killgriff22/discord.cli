import colorama
import discord
from config import *
import MultiTerm
import os
from discord.ext import tasks
valid_hex = '0123456789ABCDEF'.__contains__
def cleanhex(data):  # used for cleaning the hexadecimal color codes for fore_fromhex()
    return ''.join(filter(valid_hex, data.upper()))

def getcolor(user):  # gets the top role color from the user
    return str(user.top_role.color)

def fore_fromhex( hexcode):  # used for generating the role colors
    """print in a hex defined color"""

    if hexcode == "#000000":
        return "\033[38;2;0;0;0;48;2;255;255;255m"
    elif hexcode == "#FFFFFF":
        return colorama.Fore.BLACK+colorama.Back.WHITE
    hexint = int(cleanhex(hexcode), 16)
    return ("\x1B[48;2;{};{};{}m".format(hexint >> 16,
                                                  hexint >> 8 & 0xFF,
                                                  hexint & 0xFF))
