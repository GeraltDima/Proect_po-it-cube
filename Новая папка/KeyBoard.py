from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_1 = KeyboardButton("Направления")
button_2 = KeyboardButton("О IT-Cube🎲")
button_3 = KeyboardButton("⬅️Назад")

menu_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_1, button_2).add(button_3)

b_4 = KeyboardButton("")
b_5 = KeyboardButton("")
b_6 = KeyboardButton("")
b_7 = KeyboardButton("")
b_8 = KeyboardButton("")
b_9 = KeyboardButton("")
b_10 = KeyboardButton("")

menu_kb2 = ReplyKeyboardMarkup(resize_keyboard=True).add(b_4, b_5, b_6, b_7,b_8, b_9, b_10)