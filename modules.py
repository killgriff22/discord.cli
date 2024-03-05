import colorama
import discord
from config import *
import MultiTerm
import os
from discord.ext import tasks
valid_hex = '0123456789ABCDEF'.__contains__
currentguild = 604338503031062665
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
selection_box = MultiTerm.Screen((width, height-2), (0, 1))
mode = 0
channel_index=0