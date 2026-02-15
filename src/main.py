import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

from bot_for_test_python.src.keyboards import get_inline_keyboard, get_reply_keyboard

load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен бота (замените на свой)
BOT_TOKEN = os.getenv("TOKEN_BOT")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n"
        f"Я простой бот с кнопками для теста:",
        reply_markup=get_reply_keyboard(),
    )


@dp.message(lambda message: message.text == "Я красная кнопка")
async def reply_contacts(message: Message):
    await message.answer("тут все красное", reply_markup=get_inline_keyboard())


# Обработчик всех остальных сообщений
@dp.message()
async def echo_message(message: Message):
    await message.answer("я иничего не умею", reply_markup=get_reply_keyboard())


# Функция запуска бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
