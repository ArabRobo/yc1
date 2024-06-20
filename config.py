# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7469977300:AAGfazAHesMqbBWyw3wqw8vE-i5xmCDnWi4")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26730559"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "54e0fd326f54b4ea91fdcbdf98e3cf4e")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002034218262"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Dhilnihnge")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://dnrlevsz:ulaFWGo11hKJEthQm561hznU3jYYMJFn@john.db.elephantsql.com/dnrlevsz")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001851543827"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1002029313422"))

# Tulisan joinnya mau gimana
BUTTONS_JOIN_TEXT = os.environ.get("BUTTONS_JOIN_TEXT", "ᴊᴏɪɴ")
BUTTONS_JOIN_TEXT2 = os.environ.get("BUTTONS_JOIN_TEXT2", "ᴊᴏɪɴ")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>\n\n<b>Order Fsub : @Arabnihnge</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6655434628").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat Vidio yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu Lalu Klik Coba Lagi</b>\n\nOrder Fsub : @Arabnihnge",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
