import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env')
elif os.path.exists("sample.env"):
    load_dotenv("sample.env")

API_ID = os.getenv("21707624")
API_HASH = os.getenv("84647ccc68eae30713d82b2f134ab23c")
BOT_TOKEN = os.getenv("8115989407:AAEVHhWA2KHpUFPRZmdieKiV08OD8Auqzq0")
MONGO_DB_URI = os.getenv("mongodb+srv://beatanimes:wu0r1n5Z0QyKLkCk@cluster0.s1rifnt.mongodb.net/?appName=Cluster0")
STATUS_MSG_ID = os.getenv("2")
SCHEDULE_MSG_ID = os.getenv("3")
CHANNEL_TITLE = os.getenv("CHANNEL_TITLE", "Beat Animes")
INDEX_CHANNEL_USERNAME = os.getenv("@BeatAnimes")
UPLOADS_CHANNEL_USERNAME = os.getenv("https://t.me/+raD-tyY7z6RhOWNl")
TECHZ_API_KEY = os.getenv("TECHZ_API_KEY")
COMMENTS_GROUP_LINK = os.getenv("https://t.me/Beat_Animes_Discussion")
SLEEP_TIME = os.getenv("SLEEP_TIME", 60)

for k, v in {
    "21707624": API_ID,
    "84647ccc68eae30713d82b2f134ab23c": API_HASH,
    "8115989407:AAEVHhWA2KHpUFPRZmdieKiV08OD8Auqzq0": BOT_TOKEN,
    "mongodb+srv://beatanimes:wu0r1n5Z0QyKLkCk@cluster0.s1rifnt.mongodb.net/?appName=Cluster0": MONGO_DB_URI,
    "2": STATUS_MSG_ID,
    "3": SCHEDULE_MSG_ID,
    "@BeatAnimes": INDEX_CHANNEL_USERNAME,
    "https://t.me/+raD-tyY7z6RhOWNl": UPLOADS_CHANNEL_USERNAME,
    "TECHZ_API_KEY": TECHZ_API_KEY,
    "https://t.me/Beat_Animes_Discussion": COMMENTS_GROUP_LINK,
}.items():
    if not v:
        raise Exception(f"{k} not found .env file, please add it to use AutoAnimeBot")
