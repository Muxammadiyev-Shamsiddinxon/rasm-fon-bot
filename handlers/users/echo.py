from aiogram import types
from loader import dp

from aiogram import Bot, Dispatcher, executor, types
import logging

from  handlers.transliterate import to_cyrillic,to_latin
from handlers.checkWord import checkWord


@dp.message_handler()
async def imlo_bot(message: types.Message):
    word = to_cyrillic(message.text)
    result = checkWord(word)
    if result['available']:
        response = f"šā@Hacker_Attacks1āš\nā {to_latin(word.capitalize())}"
    else:
        response = f"šā@Hacker_Attacks1āš\nā{to_latin(word.capitalize())}\n"
        for text in result['matches']:
            response += f"ā {to_latin(text.capitalize())}\n"
        response += "\nYana so'z kiriting! āā"
    await message.answer(response)


