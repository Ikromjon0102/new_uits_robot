from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startKEY = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="âī¸ Ro'yxatdan o'tish"),
            KeyboardButton(text="âšī¸ Barcha kurslar"),
        ],
        [
            KeyboardButton(text="đ  Manzil")
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
            KeyboardButton(text='đ Python'),
            KeyboardButton(text='đ¸ WEB')
        ],
        [
            KeyboardButton(text="đ¨ Photoshop"),
            KeyboardButton(text="â 3dsMAX"),
            KeyboardButton(text="đģ Savodxonlik")
        ],
        [
            KeyboardButton(text="â IT English"),
            KeyboardButton(text="đ IT Matem")
        ],
        [
            KeyboardButton(text="đ Ortga")
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