from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)

# data = {
#     fullname: 'salom',
#     byear: 'alik',
#     own_phone: 'telown',
#     parants_phone: 'parant tel',
#     gender: 'male',
#     status: 'worker',
#     course: 'cs',
#     period: '2 kunda 1',
#     week: 'firstday',
#     hour: '8to10',
#     summa: 'salom',
#     adress: "Yoshlik MFY Andijon ko'cha 8-uy",
#     photo: 'http://telegra.ph//file/951662d153417ddaa8416.jpg'
# }