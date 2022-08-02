from aiogram.dispatcher.filters.state import StatesGroup,State

class PersonalData(StatesGroup):
    fullname = State()
    byear = State()
    own_phone = State()
    parents_phone = State()
    id_card = State()
    gender = State()
    social_status = State()
    course = State()
    period = State()
    summa = State()
    adress = State()
    photo = State()

