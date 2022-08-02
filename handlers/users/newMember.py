import logging
import time
import datetime

from data.spsheeds import sheet
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from data.dates import genderdata,day_course_data,course_hour_data,status_data,week_day_data,courses_data
from keyboards.default.mainKey import nextKey, startKEY
from keyboards.inline.genKey import genderKey, answerKey
from keyboards.inline.kursKey import proKey, day_course, week_day, course_hour
from keyboards.inline.s_status import s_statusKey
from keyboards.inline.yesno import answer_callback
from loader import dp, bot
from states.personalData import PersonalData
from utils.photourl import photo_link


@dp.message_handler(text = "✒️ Ro'yxatdan o'tish")
async def enter_test(msg: types.Message,state:FSMContext):
    await msg.answer("To'liq ism familiyangiz,\nExample: <b>Valiyev Salimjon Hakimjon o'g'li</b>",
                     reply_markup=ReplyKeyboardRemove())
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def enter_name(msg: types.Message, state:FSMContext):
    fullname = msg.text
    await state.update_data(
        {'fullname':fullname}
    )
    await msg.answer("Tug'ilgan kuningizni kiriting\n"
                     "Example: <b>15.12.1999</b> ")
    await PersonalData.byear.set()

@dp.message_handler(state=PersonalData.byear)
async def enter_name(msg: types.Message, state:FSMContext):
    byear = msg.text
    await state.update_data(
        {'byear':byear}
    )
    await msg.answer(f"<b>O'zingizni</b> telefon nomeriz\n"
                     f"Namuna: <b>99 999 7788</b>")
    await PersonalData.own_phone.set()

@dp.message_handler(state=PersonalData.own_phone)
async def answ(call: types.Message,state:FSMContext):
    own_phone = call.text
    await state.update_data(
        {'own_phone': own_phone}
    )
    await call.answer(f"<b>Ota - Onangizni</b> telefon nomeri\n"
                     f"Namuna: <b>99 999 7788</b>\n"
                     f"Namuna: <b>99 999 7788</b>")
    await PersonalData.parents_phone.set()

@dp.message_handler(state=PersonalData.parents_phone)
async def answ(msg: types.Message,state:FSMContext):
    parants_phone = msg.text
    await state.update_data({'parants_phone': parants_phone})
    await msg.answer("Metrka yoki Passport seria nomerini kiriting ",reply_markup=nextKey)
    await PersonalData.next()

@dp.message_handler(state=PersonalData.id_card)
async def answ(msg: types.Message, state: FSMContext):
    id_card = msg.text
    await state.update_data({'id_card': id_card})
    if id_card == "O'tkazib Yuborish":
        await msg.answer("Siz metrka yoki passport ma'lumotini kiritmadingiz!",reply_markup=ReplyKeyboardRemove())
        await msg.answer("Jinsingiz", reply_markup=genderKey)
        await PersonalData.gender.set()
    else:
        await msg.answer("Endi Jinsingizni tanlang",reply_markup=ReplyKeyboardRemove())
        await msg.answer("Jinsingiz",reply_markup=genderKey)
        await PersonalData.gender.set()

@dp.callback_query_handler(state=PersonalData.gender)
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    cal = call.data
    await state.update_data(
        {'gender':cal}
    )
    await call.message.delete()
    await call.message.answer("Ijtimoiy holatingiz",
                              reply_markup=s_statusKey)
    await PersonalData.next()

@dp.callback_query_handler(state=PersonalData.social_status)
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    s_status = call.data
    await call.message.delete()
    await state.update_data(
        {'status':s_status}
    )
    await call.message.answer("Kurslardan birini tanlang",
                              reply_markup=proKey)
    await PersonalData.next()
@dp.callback_query_handler(state=PersonalData.course)
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    course = call.data
    await call.message.delete()
    await state.update_data(
        {'course':course}
    )
    await call.message.answer("O'qish kunlarini tanlang",
                              reply_markup=day_course)
    await PersonalData.next()

@dp.callback_query_handler(state=PersonalData.period)
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    period = call.data
    await call.message.delete()
    logging.info(period)
    if period == "1in2":
        await state.update_data({'period': "2 kunda 1"})
        await call.message.answer("Hafta kunlarini tanlang",reply_markup=week_day)
        await state.set_state("Course_Week")
    else:
        await state.update_data({'period': "Har kuni","week":""})
        await call.message.answer("Kurs vaqtini tanlang", reply_markup=course_hour)
        await state.set_state("Course_Hour")

@dp.callback_query_handler(state="Course_Week")
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    week = call.data
    await call.message.delete()
    await state.update_data({'week': week})
    await call.message.answer("Kurs vaqtini tanlang", reply_markup=course_hour)
    await state.set_state("Course_Hour")

@dp.callback_query_handler(state="Course_Hour")
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    hour = call.data
    await call.message.delete()
    await state.update_data({'hour': hour})
    await call.message.answer("Kurs narxini kiriting\n"
                              "<b>Example: 175000 </b>")
    await PersonalData.summa.set()

@dp.message_handler(state=PersonalData.summa)
async def shsumma(msg: types.Message,state:FSMContext):
    summa = msg.text
    await state.update_data({"summa":summa})
    await msg.answer("Manzilingizni kiriting: \n<b>Namuna: Yoshlik MFY Andijon ko'cha 8-uy</b>")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.adress)
async def shadress(msg: types.Message,state:FSMContext):
    adress = msg.text
    await state.update_data({"adress":adress})
    await msg.answer("Rasm Yuklang")
    await PersonalData.next()

@dp.message_handler(content_types="photo",state=PersonalData.photo)
async def member_photo(msg:types.Message, state:FSMContext):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    await state.update_data({"photo": link})

    # # ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    # logging.info(data)
    fullname = data.get("fullname")
    byear = data.get('byear')
    own_phone= data.get('own_phone')
    parants_phone= data.get('parants_phone')
    gender= genderdata.get(data.get('gender'))
    status= status_data.get(data.get('status'))
    course= courses_data.get(data.get('course'))
    period= data.get('period')
    week= week_day_data.get(data.get('week'))
    hour= course_hour_data.get(data.get('hour'))
    summa= data.get('summa')
    adress= data.get('adress')
    photo= data.get('photo')
    id = msg.from_user.id
    card_id = data.get("id_card")
    reg_time = str(datetime.datetime.now())
    # if card_id != None:
    newmember = [id,fullname.title(),byear,card_id,own_phone,parants_phone,gender,adress,status,course,
             period,week,hour,summa,photo,reg_time]
    sheet.append_row(newmember)
        # else:
        #     newmember = [id, fullname.title(), byear, "None", own_phone, parants_phone, gender, adress, status, course,
        #                  period, week, hour, summa, photo, reg_time]
        #     sheet.append_row(newmember)
    xabar = "Quyidagi ma'lumotlar qabul qilindi:\n"
    xabar += f"Ismingiz - <b>{fullname.title()}</b>\n"
    xabar += f"Tanlagan Kursingiz - <b>{course}</b>\n"
    xabar += f"Jinsingiz - <b>{gender}</b>\n"
    xabar += f"Tug'ilgan yilingiz - <b>{byear}</b>\n"
    xabar += f"Telefon - <b>{own_phone}</b>\n"
    xabar += f"Manzilingiz - <b>{adress}</b>\n"
    xabar += f"Tanlagan vaqtingiz - <b>{hour}</b>\n"
    await msg.answer(xabar, reply_markup=startKEY)
    await bot.send_message(351602044,xabar)
    await state.finish()
    if course=="Python":
        await dp.bot.send_message(92473435, xabar)
    elif course=="Web dasturlash":
        await dp.bot.send_message(1837827627, xabar)
    elif course=="Kompyuter savodxonligi":
        await dp.bot.send_message(1009831331, xabar)
    await state.finish()
