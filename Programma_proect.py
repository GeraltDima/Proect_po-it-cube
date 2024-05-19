import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from config import TOKEN

import KeyBoard as kb
from Texts import direction_1, direction_2, direction_3, direction_4, direction_5, direction_6, direction_7, about_us, full_directions

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.reply("Привет! Нажми сюда➡️/help⬅️ чтобы узнать для чего создан этот бот!", reply_markup=kb.menu_kb1)


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.reply("Данный бот отправляет разную информацию о IT-Cube", reply_markup=kb.inline_kb)

@dp.message(F.text == 'Направления')
async def direction(message: Message):
    await message.answer(full_directions, reply_markup=kb.menu_kb2)


#============================================================================

@dp.message(F.text == 'О IT-Cube🎲')
async def info_0(message: Message):
    await message.answer(about_us)

#=================||===============================||======================
#=================||=====Н-А-П-Р-А-В-Л-Е-Н-И-Я=====||======================
#=================\/===============================\/======================

@dp.message(F.text == 'Программирование на Python')
async def info_1(message: Message):
    await message.answer(direction_1, reply_markup=kb.inline_kb1)

@dp.callback_query(F.data == 'info1')
async def clb_info1(callback: CallbackQuery):
    await callback.answer("Преподователь: Велиев Рафаель Ибрагимович\n2 группы; в одной группе - 12 человек", show_alert=True)

#============================================================================
@dp.message(F.text == 'VR/AR-разработка')
async def info_2(message: Message):
    await message.answer(direction_2, reply_markup=kb.inline_kb2)

@dp.callback_query(F.data == 'info2')
async def clb_info2(callback: CallbackQuery):
        await callback.answer("Преподователь: ФИО\n2 группы; в одной группе - 12 человек", show_alert=True)

# ============================================================================

@dp.message(F.text == 'Веб-разработка')
async def info_3(message: Message):
    await message.answer(direction_3, reply_markup=kb.inline_kb3)

@dp.callback_query(F.data == 'info3')
async def clb_info3(callback: CallbackQuery):
        await callback.answer("Преподователь: Елизаров Даниил Александрович\n2 группы; в одной группе - 12 человек", show_alert=True)

#============================================================================

@dp.message(F.text == 'Мобильная разработка')
async def info_4(message: Message):
    await message.answer(direction_4, reply_markup=kb.inline_kb4)

@dp.callback_query(F.data == 'info4')
async def clb_info4(callback: CallbackQuery):
        await callback.answer("Преподователь: ФИО\n2 группы; в одной группе - 12 человек", show_alert=True)

#============================================================================

@dp.message(F.text == 'Системное администрирование')
async def info_5(message: Message):
    await message.answer(direction_5, reply_markup=kb.inline_kb5)

@dp.callback_query(F.data == 'info5')
async def clb_info5(callback: CallbackQuery):
        await callback.answer("Преподователь: Бобровский Александр Владимирович\n2 группы; в одной группе - 12 человек", show_alert=True)

#============================================================================

@dp.message(F.text == 'Беспилотные авиационные системы')
async def info_6(message: Message):
    await message.answer(direction_6, reply_markup=kb.inline_kb6)

@dp.callback_query(F.data == 'info6')
async def clb_info6(callback: CallbackQuery):
        await callback.answer("Преподователь: Буистов Владислав Валерьевич\n2 группы; в одной группе - 12 человек", show_alert=True)

#============================================================================

@dp.message(F.text == '3D-моделирование')
async def info_7(message: Message):
    await message.answer(direction_7, reply_markup=kb.inline_kb7)

@dp.callback_query(F.data == 'info7')
async def clb_info7(callback: CallbackQuery):
        await callback.answer("Преподователь: ФИО\n2 группы; в одной группе - 12 человек", show_alert=True)

#============================================================================

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())