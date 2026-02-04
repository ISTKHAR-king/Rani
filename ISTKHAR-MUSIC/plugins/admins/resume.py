# -----------------------------------------------
# 🔸 SUKKUMusic Project
# 🔹 Developed & Maintained by: THUNDER ISTKHAR (https://github.com/itzISTKHAR)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzISTKHAR
# -----------------------------------------------
from pyrogram import filters
from pyrogram.types import Message
from ISTKHAR-MUSIC import app
from ISTKHAR-MUSIC.core.call import ISTKHAR
from ISTKHAR-MUSIC.utils.database import is_music_playing, music_on
from ISTKHAR-MUSIC.utils.decorators import AdminRightsCheck
from ISTKHAR-MUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await ISTKHAR.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
