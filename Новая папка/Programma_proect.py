from aiogram import Dispatcher, Bot, executor, types
from config import TOKEN
from KeyBoard import menu_kb1
from Texts import direction_1, direction_2, direction_3, direction_4, direction_5, direction_6, direction_7, about_us, full_directions

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await msg.reply("Привет! Нажми сюда➡️/help⬅️ чтобы узнать для чего создан этот бот!")


@dp.message_handler(commands=['help'])
async def help_command(msg:types.Message):
    await msg.reply("Данный бот отправляет разную информацию о IT-Cube", reply_markup=menu_kb1)

@dp.message_handler(text=['Направления'])
async def direction(msg:types.Message):
    await msg.answer(full_directions, )

@dp.message_handler(text=['О IT-Cube🎲'])
async def info_1(msg:types.Message):
    await msg.answer(about_us)

@dp.message_handler(text=['Программирование на Python'])
async def info_1(msg:types.Message):
    await msg.answer(direction_1)

@dp.message_handler(text=['VR/AR-разработка'])
async def info_2(msg:types.Message):
    await msg.answer(direction_2)

@dp.message_handler(text=['Веб-разработка'])
async def info_3(msg:types.Message):
    await msg.answer(direction_3)

@dp.message_handler(text=['Мобильная разработка'])
async def info_4(msg:types.Message):
    await msg.answer(direction_4)

@dp.message_handler(text=['Системное администрирование'])
async def info_5(msg:types.Message):
    await msg.answer(direction_5)

@dp.message_handler(text=['Беспилотные авиационные системы'])
async def info_1(msg:types.Message):
    await msg.answer(direction_6)

@dp.message_handler(text=['3D-моделирование'])
async def info_6(msg:types.Message):
    await msg.answer(direction_7)



if __name__ == '__main__':
    executor.start_polling(dp)