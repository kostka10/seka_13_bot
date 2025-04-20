from aiogram import Bot, Dispatcher, executor, types
import logging
import os

# Токен ми потім додамо на Render (автоматично)
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("Привіт! Це бот для гри в Секу.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
