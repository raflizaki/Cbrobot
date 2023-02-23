import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/fe73013dd30cbec4d9f50.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm 𝚁𝙰𝙼𝙱𝙴𝙻 𝚁𝙾𝙱𝙾𝚃.** \n\n"
  TEXT += "✘ **I'm Working Properly** \n\n"
  TEXT += f"✘ **My Master : [sena-ex](https://t.me/excrybaby)** \n\n"
  TEXT += f"✘ **Library Version :** `{telever}` \n\n"
  TEXT += f"✘ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"✘ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**🇮🇩Thanks For Adding Me Here 🇮🇩**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Trymaskosbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/pantekyks")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
