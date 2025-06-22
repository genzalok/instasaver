
import os
from typing import List

API_ID = os.getenv("API_ID", "29236719")
API_HASH = os.getenv("API_HASH", "1ccf1bd0a86af974e3210a55f662c062")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7604228341:AAHuywd6aBuN9Q6Qu91BExzWG-BXbq7_SSc")
ADMIN = int(os.getenv("ADMIN", "1296545302"))

CHNL_LINK = os.getenv("CHNL_LINK", "https://t.me/filmyrip_official")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002289220626"))
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002297551055"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://instasaver:insta273155@cluster0.eex0xzx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") #MongoDB URL
DB_NAME = os.getenv("DB_NAME", "instasaver")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002001028091").split())) # Add Multiple channel id

REEL_AUTO_DELETE = int(os.getenv("REEL_AUTO_DELETE", "600")) #10min

"""
This code is created and owned by @anonymousxbring. Do not remove or modify the credit.

Removing the credit does not make you a developer; it only shows a lack of respect for real developers.
  
Respect the work. Keep the credit.

"""
