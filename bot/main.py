import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers import commands, buttons
import mysql.connector
from mysql.connector import Error
load_dotenv()

db = mysql.connector.connect(
    host = getenv("host"),
    user = getenv("user"),
    passwd = getenv("passwd"),
    port = getenv("port"),
    database = getenv("database")
)
if db.is_connected():
    db_Info = db.get_server_info()
    print("✅ | Mysql connection -> ", db_Info)
    cursor = db.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("📝 | Database Name -> ", record)

TOKEN = getenv("TG_TOKEN")

if not TOKEN:
    logging.error("❌ | No BOT_TOKEN provided")
    sys.exit(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

commands.register_handlers(dp)
buttons.register_handlers(dp)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    print("✅ | Bot connected")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, stream=sys.stdout)
    asyncio.run(main())
