from aiogram import Router, F, BaseMiddleware

from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    TelegramObject,
)

from typing import Callable, Awaitable, Dict, Any

from dbrequests import update_db

router_client = Router()


def create_module_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1 модуль', callback_data='1 модуль'),
         InlineKeyboardButton(text='2 модуль', callback_data='2 модуль'),
         InlineKeyboardButton(text='3 модуль', callback_data='3 модуль')],

        [InlineKeyboardButton(text='4 модуль', callback_data='4 модуль'),
         InlineKeyboardButton(text='5 модуль', callback_data='5 модуль'),
         InlineKeyboardButton(text='6 модуль', callback_data='6 модуль')],

        [InlineKeyboardButton(text='7.1 модуль', callback_data='7_1 модуль'),
         InlineKeyboardButton(text='7.2 модуль', callback_data='7_2 модуль'),
         InlineKeyboardButton(text='7.3 модуль', callback_data='7_3 модуль')],

        [InlineKeyboardButton(text='8 модуль', callback_data='8 модуль')]
    ])


MODULES_DESCRIPTION = """Курс-хаб: https://e.vyatsu.ru/course/view.php?id=31975

1 модуль - основы программирования на Python
2 модуль - основы алгоритмизации
3 модуль - базы данных и реляционная алгебра
4 модуль - cтандартные библиотеки Python
5 модуль - моделирование бизнес-процессов
6 модуль - разработка баз данных
7.1 модуль - анализ данных
7.2 модуль - UI/UX-дизайн
7.3 модуль - Основы веб-разработки
8 модуль - практика в профильной сфере"""


async def send_or_edit_modules_message(message, keyboard):
    if isinstance(message, Message):
        await message.answer(MODULES_DESCRIPTION, reply_markup=keyboard)
    elif isinstance(message, CallbackQuery):
        await message.message.edit_text(MODULES_DESCRIPTION, reply_markup=keyboard)
        await message.answer()


@router_client.message(F.text == '/start')
async def start_handler(message: Message):
    keyboard = create_module_keyboard()
    await send_or_edit_modules_message(message, keyboard)


@router_client.callback_query(F.data == 'Меню')
async def menu_handler(callback: CallbackQuery):
    keyboard = create_module_keyboard()
    await send_or_edit_modules_message(callback, keyboard)
