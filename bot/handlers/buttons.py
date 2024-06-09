from aiogram import types, Dispatcher

async def handle_profile_button(message: types.Message):
    await message.answer("This is your profile.")

async def handle_statistics_button(message: types.Message):
    await message.answer("These are your statistics.")

async def handle_add_transaction_button(message: types.Message):
    await message.answer("You can add a transaction here.")

def register_handlers(dp: Dispatcher):
    dp.message.register(handle_profile_button, lambda message: message.text == "🏷️Profile")
    dp.message.register(handle_statistics_button, lambda message: message.text == "📊Statistics")
    dp.message.register(handle_add_transaction_button, lambda message: message.text == "💸Add transaction")
