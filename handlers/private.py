import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/be58748bc2dabc2d3ef4c.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━
 ʜᴇʏ, ɪ ᴀᴍ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs...
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ /
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [Sᴛᴀʀ Bᴏɪ](https://t.me/Tommy_Shelbee)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/Lost_Kiddo) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url="https://t.me/AngelxRobot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "Cʀᴇᴀᴛᴏʀ👽", url="https://t.me/ThomasShebLYY"
                    ),
                    InlineKeyboardButton(
                        "Hᴇᴀᴠᴇɴ 🚑", url="https://t.me/angelsupports"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ Cᴏᴅᴇ😹", url="https://t.me/addstickers/vibeexepart2_by_fStikBot"
                    )]
            ]
       ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/970edfeabab296b03b987.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ Cᴏᴅᴇ😹", url=f"https://t.me/addstickers/vibeexepart2_by_fStikBot")
                ]
            ]
        ),
    )

@Client.on_message(filters.command("ping") & ~filters.private & ~filters.channel & ~filters.group)
async def gstart(_, message: Message):
      await message.reply_text("""**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛs♬", url="https://t.me/angelsupports")
                ]
            ]
        )
   )
