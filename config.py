"""
from os import getenv


API_ID = int(getenv("API_ID", "13460015"))
API_HASH = getenv("API_HASH", "bd452af645d2a569f654f70b366ce577")
BOT_TOKEN = getenv("BOT_TOKEN", "7581825946:AAHzGwkqx4Rs-4Dx7pjZaq52SQOJ60H6cWs")
OWNER_ID = int(getenv("OWNER_ID", "6749313249"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6749313249 5431970720").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://mariogamerhome:z2nQreOIbwy9OzgR@cluster0.lqfpvlc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002640138333"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002640138333"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

