from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKey import  mainKey,startKEY
from loader import dp


@dp.message_handler(text="ℹ️ Barcha kurslar")
async def start(message: types.Message):
    await message.answer("Quyida kurslar haqida Ma'lumot olishingiz mumkin",
                         reply_markup=mainKey)

@dp.message_handler(text="🏠 Manzil")
async def start(message: types.Message):
    await message.answer_location(latitude=41.107565,longitude=72.078584)
    await message.answer("🏠 Bizning manzil: Uchqo'rg'on shahar Andijon ko'cha 8-uy \n"
                         "Sobiq Uchqo'rg'on iqtisodiyot kolleji (TEXNIKUM) binosida"
                         "Murojaat uchun : +998 91 360 42 54",
                         reply_markup=startKEY)

@dp.message_handler(text="🔙 Ortga")
async def start(message: types.Message):
    await message.answer("Quyida kurslar haqida Ma'lumot olishingiz mumkin",
                         reply_markup=startKEY)
