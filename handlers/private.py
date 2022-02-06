import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6aa58247f23fd76034c9.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [✨ 𝐀𝐛𝐡𝐢 𝐑𝐚𝐧𝐚 ❤️](https://t.me/Itz_Venom_xD)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [✨ 𝐀𝐛𝐡𝐢 𝐑𝐚𝐧𝐚](https://t.me/Itz_Venom_xD)
𝐎𝐰𝐧𝐞𝐫 :- [✨ ❛-𝐌𝐫𝐬'𝐂𝐚𝐧𝐝𝐲](https://t.me/Candy_626)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [✨  𝐑𝐨𝐜𝐤𝐬 🎧](https://t.me/Shayri_Music_Lovers)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [✨  𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗥𝗲𝗽𝗼 🌍](https://github.com/CandyMusic/CandyPrivateMusic)
𝐂𝐡𝐚𝐧𝐧𝐞𝐥 :- [✨𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗡𝗼𝘄 🚩](https://t.me/Shayri_Music_Lovers)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [✨ 𝗝𝗼𝗶𝗻 ❤️🥀](https://t.me/AlishaSupport)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [❛-𝐌𝐫𝐬'𝐂𝐚𝐧𝐝𝐲 🍬](https://t.me/Candy_626)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/CandyMusic_Robot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/218b5b460d60e7ea68831.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐂𝐥𝐢𝐜𝐤 𝐑𝐞𝐩𝐨 💞", url=f"https://github.com/CandyMusic/candyMusicPlayer")
                ]
            ]
        ),
    )
