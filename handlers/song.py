import os
import requests
import aiohttp
import yt_dlp

from pyrogram import filters, Client
from youtube_search import YoutubeSearch

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command('song') & ~filters.private & ~filters.channel)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("𝗙𝗜𝗡𝗗𝗜𝗡𝗚 𝗧𝗛𝗘 🎧 𝗦𝗢𝗡𝗚 𝗙𝗥𝗢𝗠 🍷𝗨𝗥𝗔𝗡𝗜𝗨𝗠 𝗦𝗘𝗥𝗩𝗘𝗥🍷...")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "𝗦𝗢𝗡𝗚 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 👀."
        )
        print(str(e))
        return
    m.edit("🍷𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙵𝚁𝙾𝙼 𝚄𝚁𝙰𝙽𝙸𝚄𝙼 𝚂𝙴𝚁𝚅𝙴𝚁🍷...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = "**🎧𝐒𝐎𝐍𝐆 𝐔𝐏𝐋𝐎𝐀𝐃 𝐁𝐘 :- ✨ [🍷𝗨𝗥𝗔𝗡𝗜𝗨𝗠🍷](https://t.me/DAZZLING_GALAXY) ❤️**"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit("**𝐘𝐎𝐔𝐓𝐔𝐁𝐄 𝐄𝐑𝐑𝐎𝐑 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐎𝐖𝐍𝐄𝐑 [🍷𝗨𝗥𝗔𝗡𝗜𝗨𝗠🍷](https://t.me/DAZZLING_GALAXY) ❤️**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
