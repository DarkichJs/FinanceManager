import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers import commands, buttons

load_dotenv()

TOKEN = getenv("TG_TOKEN")

if not TOKEN:
    logging.error("No BOT_TOKEN provided. Please set the BOT_TOKEN environment variable.")
    sys.exit(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

commands.register_handlers(dp)
buttons.register_handlers(dp)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
