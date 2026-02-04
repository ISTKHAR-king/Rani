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
from ISTKHAR-MUSIC import app
from ISTKHAR-MUSIC.misc import SUDOERS
from ISTKHAR-MUSIC.utils.database import add_off, add_on
from ISTKHAR-MUSIC.utils.decorators.language import language


@app.on_message(filters.command(["logger"]) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
