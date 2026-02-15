import asyncio
import logging
import os
from tkinter.ttk import Style
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен бота (замените на свой)
BOT_TOKEN = os.getenv("TOKEN_BOT")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создание обычной клавиатуры (ReplyKeyboard)
def get_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Я красная кнопка", style="danger", icon_custom_emoji_id="5875323095501247167")],
            [KeyboardButton(text="Я синия кнопка", style="primary", icon_custom_emoji_id="5197247368344379154")], 
            [KeyboardButton(text="Я зеленая кнопки ", style="success", icon_custom_emoji_id="5388977792224342481")]
        ],
        resize_keyboard=True,  # Автоматически подгонять размер
        input_field_placeholder="Выберите действие..."
    )
    return keyboard

def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Youtube", url="https://example.com", style="danger", icon_custom_emoji_id="5411222239599168125")],
            [InlineKeyboardButton(text="Telegram канал", url="https://t.me/example", style="primary", icon_custom_emoji_id="5884356309372900807")],
            [InlineKeyboardButton(text="Вацап", callback_data="help", style="success", icon_custom_emoji_id="5388888315170665675")]
        ]
    )
    return keyboard


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n"
        f"Я простой бот с кнопками для теста:",
        reply_markup=get_reply_keyboard()
    )

@dp.message(lambda message: message.text == "Я красная кнопка")
async def reply_contacts(message: Message):
    await message.answer(
        "тут все красное",
        reply_markup=get_inline_keyboard()
    )

# Обработчик всех остальных сообщений
@dp.message()
async def echo_message(message: Message):
    await message.answer(
        "я иничего не умею",
        reply_markup=get_reply_keyboard()
    )

# Функция запуска бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())