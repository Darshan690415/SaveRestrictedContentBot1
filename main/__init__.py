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
BOT_TOKEN = "7396421147:AAGAeJQbnNpmWwEGmIfN4MHj5ARN0e1RXC0"
SESSION = "BQEtWHgAj_jU8Qg91EdnL56hEhHCYgaueh_j621BwC60jEqFnHgPvhpw3KsOuIw0bLHRL9JK-X4YrZgkJ7cOSWopS9rI1XeKs1R9Sa7Ob3urGMarqOYJUpmqqPWZVLKa_QoE8tIQc70YGairjXYZt51k9Kjkh0PJevHtU0ex00cG3hFCjALaZ42Vacz_xrefFeCMT6b6oqEZRU8FX1Qo0fa4OB3lufQWvaE5CPZWczx6V-C9QPmIxfi9tXaz6mSzO4tbIgK13mcsCZmjen_tdPSw_nHh2GnwF2m6kIzSoceM6K7PyLzyaGfceiYdLtHUW9ad5EnVti6RrtKqz-7Mnk-uOxtL1QAAAAFrTgnxAA"
FORCESUB = "Bing"
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
