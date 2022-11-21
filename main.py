from asyncio import new_event_loop
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

loop = new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
