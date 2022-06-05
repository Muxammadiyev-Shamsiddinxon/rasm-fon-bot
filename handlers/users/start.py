from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalom alaykum, <b>{message.from_user.full_name.title()}</b>\nBot Rasm-ni orqa fonini o'chiradi.")
