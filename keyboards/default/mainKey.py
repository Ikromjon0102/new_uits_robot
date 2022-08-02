from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startKEY = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✒️ Ro'yxatdan o'tish"),
            KeyboardButton(text="ℹ️ Barcha kurslar"),
        ],
        [
            KeyboardButton(text="🏠 Manzil")
        ]
    ],resize_keyboard=True
)
# startKey = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Contact",request_contact=True),
#             # KeyboardButton(text="location",request_location=True),
#         ]
#     ], resize_keyboard=True
# )
mainKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🐍 Python'),
            KeyboardButton(text='🕸 WEB')
        ],
        [
            KeyboardButton(text="🎨 Photoshop"),
            KeyboardButton(text="✒ 3dsMAX"),
            KeyboardButton(text="💻 Savodxonlik")
        ],
        [
            KeyboardButton(text="✈ IT English"),
            KeyboardButton(text="📐 IT Matem")
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ], resize_keyboard=True
)
nextKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'tkazib Yuborish")
        ]
    ],resize_keyboard=True
)