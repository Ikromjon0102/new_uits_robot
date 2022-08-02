from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

proKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🐍 Python',callback_data="py"),
        ],
        [
            InlineKeyboardButton(text='🕸 WEB',callback_data="web")
        ],
        [
            InlineKeyboardButton(text="🎨 Photoshop",
                                 callback_data="pshop")
        ],
        [
            InlineKeyboardButton(text="✒ 3dsMAX",
                                 callback_data="3ds")
        ],
        [
            InlineKeyboardButton(text="💻 Savodxonlik",
                                 callback_data="cs")
        ],
        [
            InlineKeyboardButton(text="✈ IT English",
                                 callback_data="eng"),
        ],
        [
            InlineKeyboardButton(text="📐 IT Matem",
                                 callback_data="math")
        ],
        # [
        #     InlineKeyboardButton(text=" Chanel",
        #                          url="https://t.me/UIT_School"),
        #     InlineKeyboardButton(text="Group",
        #                          url="https://t.me/UITS_live_chat")
        # ],
        # [
        #     InlineKeyboardButton(text=" Share",
        #         switch_inline_query="Zo'r bot ekan"),
        # ],
    ]
)




day_course = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="2 kunda 1", callback_data="1in2"),
            InlineKeyboardButton(text="Har kunlik", callback_data="allday"),
        ]
    ]
)
week_day = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Dushanba, Chorshanba, Juma", callback_data="firstday")
        ],
        [
            InlineKeyboardButton(text="Seshanba, Payshanba, Shanba", callback_data="secondday"),
        ]
    ]
)
course_hour = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="8-10 gacha", callback_data="8to10"),
            InlineKeyboardButton(text="10-12 gacha", callback_data="10to12")
        ],
        [
            InlineKeyboardButton(text="13-15 gacha", callback_data="13to15"),
            InlineKeyboardButton(text="15-17 gacha", callback_data="15to17")
        ],
        [
            InlineKeyboardButton(text="Ixtiyoriy vaqtda",callback_data='notatall')
        ]
    ]
)
