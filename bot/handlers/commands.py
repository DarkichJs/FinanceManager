from aiogram import types, Dispatcher
from aiogram.filters import Command

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

def register_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
