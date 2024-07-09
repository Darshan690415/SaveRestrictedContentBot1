#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "25352517"
API_HASH = "2b7e6cf7752c3af91f958d67793a3e0b"
BOT_TOKEN = "7453258851:AAHBn_uEs9gmCtjKN-MOKJOaeQnXdL85axk"
SESSION = "BQGC2UUAdrvJD9dW_OKTBB5gQBtivIpwL_-TU5JAVc7KLZjiPv3VCkvHdLRCj9OM28nWU06jZyONzxYX91XpeqiaGCDk5K5biQpujELG0d9FKUETVf_tmNKCR8bl3I9xxbpWeSbrxTa4H9nv4NQtfiUr991lbCGIWgJWMRmEcyyNY_8smWnk0ozaYg8M-4yBXfzpt5I73d7QowqHagcbuDd0ouqc1JC-dQ0VxERQHhe81IHzAgAkcSofu39BT3gPrwr2WW34vLW4BbGURDOomYHLvcfkxcIsMniSWiGtVBqc4XzwTiNBuOfiftBl8C0JjJJUY4vfUAhfqCi1Xyls6e8bm39AygAAAAG8P7RjAQ"
FORCESUB = "might"
AUTH = "6095243761"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
