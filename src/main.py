import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

from keyboards import get_inline_keyboard, get_reply_keyboard

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

    user = message.from_user

    # Формируем информацию о пользователе
    user_info = (
        f"🆕 **Новый пользователь запустил бота!**\n"
        f"┌ 👤 **Имя:** {user.full_name}\n"
        f"├ 🆔 **ID:** `{user.id}`\n"
        f"├ 🌍 **Язык:** {user.language_code or 'не указан'}\n"
        f"└ 🔗 **Юзернейм:** @{user.username}"
    )

    # Отправляем в группу
    await bot.send_message(os.getenv("CHAT_ID"), user_info, parse_mode="Markdown")

    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n"
        f"Я простой бот с кнопками для теста:",
        reply_markup=get_reply_keyboard(),
    )


@dp.message(lambda message: message.text == "Красная кнопка")
async def reply_contacts(message: Message):
    await message.answer("Мои социальыне сети:", reply_markup=get_inline_keyboard())


# Обработчик всех остальных сообщений
@dp.message()
async def echo_message(message: Message):
    await message.answer("тут ничего нету... ):", reply_markup=get_reply_keyboard())


# Функция запуска бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
