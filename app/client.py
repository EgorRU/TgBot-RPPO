from aiogram import Router, F, BaseMiddleware
from aiogram.filters import CommandStart
import re

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

MODULES_DESCRIPTION = """Курс-хаб: https://e.vyatsu.ru/course/view.php?id=31975

1 модуль - Основы программирования на Python
2 модуль - Основы алгоритмизации
3 модуль - Базы данных и реляционная алгебра
4 модуль - Стандартные библиотеки Python
5 модуль - Моделирование бизнес-процессов
6 модуль - Разработка баз данных
7.1 модуль - Анализ данных
7.2 модуль - UI/UX-дизайн
7.3 модуль - Основы веб-разработки
8 модуль - Практика в профильной сфере"""

data = {
    '1': {
        'message_text': '1 модуль - Основы программирования на Python\nhttps://e.vyatsu.ru/course/view.php?id=33137',
        'test': 'https://e.vyatsu.ru/mod/quiz/view.php?id=760514',
        'schedule': '',
    },
    '2': {
        'message_text': '2 модуль - Основы алгоритмизации\nhttps://e.vyatsu.ru/course/view.php?id=33138',
        'test': 'https://e.vyatsu.ru/mod/quiz/view.php?id=760553',
        'schedule': 'https://docs.google.com/spreadsheets/d/1PRkm9pfTxrnLbW8UV1fNTpxTXlrdl12kEgdDbsztKKs/edit?gid=0#gid=0',
    },
}

def create_module_keyboard(args=''):
    pattern = r"^module_[1-2]$"
    if not re.match(pattern, args):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1 модуль', callback_data='1 модуль'),
         InlineKeyboardButton(text='2 модуль', callback_data='2 модуль'),
         InlineKeyboardButton(text='3 модуль', callback_data='3 модуль')],

        [InlineKeyboardButton(text='4 модуль', callback_data='4 модуль'),
         InlineKeyboardButton(text='5 модуль', callback_data='5 модуль'),
         InlineKeyboardButton(text='6 модуль', callback_data='6 модуль')],

        [InlineKeyboardButton(text='7.1 модуль', callback_data='7_1 модуль'),
         InlineKeyboardButton(text='7.2 модуль', callback_data='7_2 модуль'),
         InlineKeyboardButton(text='7.3 модуль', callback_data='7_3 модуль')],

        [InlineKeyboardButton(text='8 модуль', callback_data='8 модуль')],

        [InlineKeyboardButton(text='Ассесмент', callback_data='Ассесмент')]
        ])
        message_text = MODULES_DESCRIPTION
    else:
        n = args[-1]
        inline_keyboard = [
            [InlineKeyboardButton(text='Лекции', callback_data=f'Лекции{n}'),
             InlineKeyboardButton(text='Материал лаб. работ', callback_data=f'Материал лаб. работ{n}')],

            [InlineKeyboardButton(text='Материалы сам. работ', callback_data=f'Материалы сам. работ{n}'),
             InlineKeyboardButton(text='Доп. материал', callback_data=f'Доп. материал{n}')],

            [InlineKeyboardButton(text='Файл с материалами', callback_data=f'Файл с материалами{n}'),
             InlineKeyboardButton(text='Тестирование', url=data[n]['test'])],
        ]
        if data[n]['schedule']:
            inline_keyboard.append([InlineKeyboardButton(text='Расписание', url=data[n]['schedule'])]),
        
        inline_keyboard.append([InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')])
        
        message_text = data[n]['message_text']
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard, message_text

    
async def send_or_edit_modules_message(message, keyboard, message_text=MODULES_DESCRIPTION):
    if isinstance(message, Message):
        await message.answer(message_text, reply_markup=keyboard)
    elif isinstance(message, CallbackQuery):
        await message.message.edit_text(message_text, reply_markup=keyboard)
        await message.answer()


@router_client.message(CommandStart())
async def start_handler(message: Message, command):
    args = command.args if command.args else ''
    keyboard, message_text = create_module_keyboard(args)
    await send_or_edit_modules_message(message, keyboard, message_text)


@router_client.callback_query(F.data == 'Меню')
async def menu_handler(callback: CallbackQuery):
    keyboard, message_text = create_module_keyboard()
    await send_or_edit_modules_message(callback, keyboard)


@router_client.callback_query(F.data == 'Ассесмент')
async def assesment_handler(callback: CallbackQuery):
    await callback.answer("С 17 февраля...", show_alert=True)
