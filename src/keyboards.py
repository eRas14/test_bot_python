from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)


# Создание обычной клавиатуры (ReplyKeyboard)
def get_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Я красная кнопка",
                    style="danger",
                    icon_custom_emoji_id="5875323095501247167",
                )
            ],
            [
                KeyboardButton(
                    text="Я синия кнопка",
                    style="primary",
                    icon_custom_emoji_id="5197247368344379154",
                )
            ],
            [
                KeyboardButton(
                    text="Я зеленая кнопка",
                    style="success",
                    icon_custom_emoji_id="5388977792224342481",
                )
            ],
        ],
        resize_keyboard=True,  # Автоматически подгонять размер
        input_field_placeholder="Выберите действие...",
    )
    return keyboard


def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Мой Youtube кана",
                    url="https://t.me/erasj",
                    style="danger",
                    icon_custom_emoji_id="5411222239599168125",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Это тоже я",
                    url="https://t.me/erasj",
                    style="primary",
                    icon_custom_emoji_id="5884356309372900807",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Отправьте мне сердечко",
                    url="https://t.me/erasj",
                    style="success",
                    icon_custom_emoji_id="5388888315170665675",
                )
            ],
        ]
    )
    return keyboard
