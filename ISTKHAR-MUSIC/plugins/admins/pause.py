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
from ISTKHAR-MUSIC.utils.database import is_music_playing, music_off
from ISTKHAR-MUSIC.utils.decorators import AdminRightsCheck
from ISTKHAR-MUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await ISTKHAR.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
