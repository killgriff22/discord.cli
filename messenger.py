from modules.handler import handler
from config import config
import asyncio
handler.login(config.TOKEN)
asyncio.run(handler.sendmessage(handler.currentguild,handler.currentchannel,"test123,this is an automated message"))