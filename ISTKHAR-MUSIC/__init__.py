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
from ISTKHAR-MUSIC.core.bot import ISTKHAR
from ISTKHAR-MUSIC.core.dir import dirr
from ISTKHAR-MUSIC.core.git import git
from ISTKHAR-MUSIC.core.userbot import Userbot
from ISTKHAR-MUSIC.misc import dbb, heroku
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR()
userbot = Userbot()
api = SafoneAPI()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "InflexOwnerBot"  # connect music api key "Dont change it"