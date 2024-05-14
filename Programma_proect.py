from aiogram import Dispatcher, Bot, executor, types
from config import TOKEN
from KeyBoard import menu_kb1


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await msg.reply("Привет, напиши /help чтобы узнать для чего этот бот!")


@dp.message_handler(commands=['help'])
async def help_command(msg:types.Message):
    await msg.reply("Данный бот отправляет разную информацию о IT-Cube", reply_markup=menu_kb1)

@dp.message_handler(commands=['Программирование на Python'])
async def info_1(msg:types.Message):
    await msg.answer("""В ходе курса вы научитесь:"
                     "- строить алгоритмы программ;"
                     "– писать чистый и грамотный код;"
                     "– работать в современных IDE;"
                     "- писать программы для решения конкретных задач""")

@dp.message_handler(commands=['VR/AR-разработка'])
async def info_1(msg:types.Message):
    await msg.answer("""В ходе курса вы научитесь:"
                     "- научитесь работать с игровыми движками (Unity и Unreal Engine);"
                     "– научитесь создавать ассеты для своих приложений (уровней или сцен);"
                     "– сможете создавать сложные сцены и уровни для виртуальной реальности""")

@dp.message_handler(commands=['VR/AR-разработка'])
async def info_1(msg:types.Message):
    await msg.answer("""""")

@dp.message_handler(text=['Направления'])
async def direction(msg:types.Message):
    await msg.answer("""Направления IT-Cube:"
                     "•Программирование на Python"
                     "•VR/AR-разработка"
                     "•Веб-разработка"
                     "•Мобильная разработка"
                     "•Системное администрирование"
                     "•Беспилотные авиационные системы"
                     "•Лицей Академии Яндекса""")


if __name__ == '__main__':
    executor.start_polling(dp)