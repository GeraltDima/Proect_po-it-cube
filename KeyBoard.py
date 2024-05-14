from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_1 = KeyboardButton("Направления")
button_2 = KeyboardButton("О IT-Cube")
menu_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1, button_2)

