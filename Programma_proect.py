import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import TOKEN

import KeyBoard as kb
from Texts import (direction_1, direction_2, direction_3, direction_4, direction_5, direction_6,
                   direction_7, about_us, full_directions)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Привет! {about_us}", reply_markup=kb.menu_kb1)


@dp.message(F.text == 'Направления')
async def direction(message: Message):
    await message.answer(full_directions, reply_markup=kb.menu_kb2)

@dp.message(F.text == 'Как поступить в IT-Cube')
async def enroll(message: Message):
    await message.answer("Адрес: г. Калининград, ул. Маршала Новикова 5\nПочта: support@it-cube39.ru\nТелефон:+7 (929) 166-03-67", reply_markup=kb.inline_kb)

#=================||===============================||======================
#=================||=====Н-А-П-Р-А-В-Л-Е-Н-И-Я=====||======================
#=================\/===============================\/======================

@dp.message(F.text == 'Программирование на Python')
async def info_1(message: Message):
    await message.answer(direction_1, reply_markup=kb.inline_kb1)

@dp.callback_query(F.data == 'info1')
async def clb_info1(callback: CallbackQuery):
    await callback.answer("Для учащихся 5-8 классов\nОбъем программы – 144 академ. часа\nПродолжительность курса – 1 год.", show_alert=True)

#============================================================================
@dp.message(F.text == 'VR/AR-разработка')
async def info_2(message: Message):
    await message.answer(direction_2, reply_markup=kb.inline_kb2)

@dp.callback_query(F.data == 'info2')
async def clb_info2(callback: CallbackQuery):
    await callback.answer("Начальный, углубленный и проектный уровни - для учащихся 7-11 классов\nОбъем программы – 144 академ. часа\nПродолжительность каждого курса – 1 год.", show_alert=True)

# ============================================================================

@dp.message(F.text == 'Веб-разработка')
async def info_3(message: Message):
    await message.answer(direction_3, reply_markup=kb.inline_kb3)

@dp.callback_query(F.data == 'info3')
async def clb_info3(callback: CallbackQuery):
    await callback.answer("Для учащихся 7-8 классов\nОбъем программы – 144 академ. часа\nПродолжительность курса – 1 год.", show_alert=True)

#============================================================================

@dp.message(F.text == 'Мобильная разработка')
async def info_4(message: Message):
    await message.answer(direction_4, reply_markup=kb.inline_kb4)

@dp.callback_query(F.data == 'info4')
async def clb_info4(callback: CallbackQuery):
    await callback.answer("Начальный уровень - для учащихся 5-6 классов\nAndroid-разработка - для учащихся 8-11 класов\nKotlin - для учащихся 9-11 классов\nОбъем программы – 144 академ. часа\nПродолжительность каждого курса – 1 год.", show_alert=True)

#============================================================================

@dp.message(F.text == 'Системное администрирование')
async def info_5(message: Message):
    await message.answer(direction_5, reply_markup=kb.inline_kb5)

@dp.callback_query(F.data == 'info5')
async def clb_info5(callback: CallbackQuery):
    await callback.answer("Начальный и углуб. уровни - для учащихся 6-11 классов\nОбъем программы – 144 академ. часа\nПродолжительность каждого курса – 1 год.", show_alert=True)

#============================================================================

@dp.message(F.text == 'Беспилотные авиационные системы')
async def info_6(message: Message):
    await message.answer(direction_6, reply_markup=kb.inline_kb6)

@dp.callback_query(F.data == 'info6')
async def clb_info6(callback: CallbackQuery):
    await callback.answer("Для учащихся 5-8 классов\nОбъем программы – 144 академ. часа\nПродолжительность курса – 1 год.", show_alert=True)

#============================================================================

@dp.message(F.text == '3D-моделирование')
async def info_7(message: Message):
    await message.answer(direction_7, reply_markup=kb.inline_kb7)

@dp.callback_query(F.data == 'info7')
async def clb_info7(callback: CallbackQuery):
    await callback.answer("Для учащихся 6-9 классов\nОбъем программы – 144 академ. часа\nПродолжительность курса – 1 год.", show_alert=True)

#============================================================================

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())