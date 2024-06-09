import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("TG_TOKEN")

if not TOKEN:
    logging.error("No BOT_TOKEN provided. Please set the BOT_TOKEN environment variable.")
    sys.exit(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="🏷️Profile"),
            types.KeyboardButton(text="📊Statistics")
        ],
        [
            types.KeyboardButton(text="💸Add transaction"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Select function"
    )
    await message.answer("Hello, keep the panel below", reply_markup=keyboard)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
