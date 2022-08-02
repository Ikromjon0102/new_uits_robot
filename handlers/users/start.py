from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKey import  startKEY
from loader import dp

# @dp.message_handler(content_types="photo")
# async def photo_(msg:types.Message):
#     photo_id = msg.photo[-1].file_id
#     await msg.answer(photo_id)
#

# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Assalomu aleykum, "
#                          f" <a href='https://t.me/UIT_School'>Uchkurgan IT School</a>ning, "
#                          f"rasmiy telegram botiga xush kelibsiz!\n"
#                          f"ushbu bot orqali <b>IT Kurslar</b>ga ro'yxatdan o'tishingiz mumkin")
#     await message.answer("Ro'yxatdan o'tish uchun <b>Contact</b>ingizni yuboring",
#                          reply_markup=startKey)
#


@dp.message_handler(content_types="photo")
async def start(message: types.Message):
    id = message.photo[-1].file_id
    await message.answer(id)

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIF7mLoHrPJm4AHBnEywmhVJ8n4dAAB4wACVcIxG078QUubck9iGkD-zAEAAwIAA3kAAykE',
                               caption=f"Assalomu aleykum, "
                                     f" <a href='https://t.me/UIT_School'>Uchkurgan IT School</a>ning, "
                                     f"rasmiy telegram botiga xush kelibsiz!\n"
                                     f"ushbu bot orqali <b>IT Kurslar</b>ga ro'yxatdan o'tishingiz mumkin",reply_markup=startKEY)