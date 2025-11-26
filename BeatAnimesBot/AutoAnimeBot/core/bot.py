from pyrogram import Client
from config import *
import asyncio
from BeatAnimeBot.modules.parser import auto_parser
from pyrogram.errors import MessageNotModified
from BeatAnimeBot.modules.tg_handler import tg_handler
from BeatAnimeBot.inline import button1
from pyrogram.types import Message
from BeatAnimeBot.core.log import LOGGER


class BeatAnimeBot(Client):
    def __init__(self):
        self.logger = LOGGER("BeatAnimeBot")
        self.logger.info("Starting BeatAnimeBot")
        super().__init__(
            "BeatAnimeBot", api_id=int(API_ID), api_hash=API_HASH, bot_token=BOT_TOKEN
        )

    async def start(self):
        await super().start()

        self.logger.info("Getting Channel IDs")
        self.INDEX_CHANNEL_ID = (await self.get_chat(INDEX_CHANNEL_USERNAME)).id
        self.UPLOADS_CHANNEL_ID = (await self.get_chat(UPLOADS_CHANNEL_USERNAME)).id

        self.logger.info("Getting Status Messages")
        self.queue = []
        self.status: Message = await self.get_messages(
            self.UPLOADS_CHANNEL_ID, int(STATUS_MSG_ID)
        )
        self.schedule: Message = await self.get_messages(
            self.UPLOADS_CHANNEL_ID, int(SCHEDULE_MSG_ID)
        )

        self.logger.info("==================================")
        self.logger.info("BeatAnimeBot Started Bot Successfully")
        self.logger.info("==========JOIN @BeatAnime=========")

        self.logger.info("Adding Parsing Task")
        asyncio.create_task(auto_parser(TECHZ_API_KEY, self))
        asyncio.create_task(tg_handler(self, TECHZ_API_KEY))

    async def update_status(self, text):
        try:
            logger = LOGGER("Status")
            logger.info(text)
            text = self.status_text(text)
            await self.status.edit_text(text, reply_markup=button1)
        except MessageNotModified:
            pass
        except Exception as e:
            logger.warning(str(e))

    def status_text(self, text):
        stat = """
⭐️ **Status :** {}

⏳ **Queue :** 

{}
    """

        queue_text = ""
        for i in self.queue[:10]:
            queue_text += "📌 " + i.replace("-", " ").title().strip() + "\n"

        if queue_text == "":
            queue_text = "❌ Empty"

        return stat.format(text, queue_text)

