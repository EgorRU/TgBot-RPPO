from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD
import sqlite3


router_client = Router()


@router_client.message(F.text == '/start')
async def start(message: Message):
    await update_BD(message, "/start")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ресурсы ВятГУ',
                                callback_data='Ресурсы ВятГУ')],
        [InlineKeyboardButton(text='Цифровые кафедры',
                                callback_data='Цифровые кафедры')],
    ])
    await message.answer("Основной раздел", reply_markup=keyboard)


@router_client.callback_query(F.data == 'Меню')
async def menu(callback: CallbackQuery):
    await update_BD(callback, "Меню")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ресурсы ВятГУ',
                                callback_data='Ресурсы ВятГУ')],
        [InlineKeyboardButton(text='Цифровые кафедры',
                                callback_data='Цифровые кафедры')],
    ])
    await callback.message.edit_text("Основной раздел", reply_markup=keyboard)
    await callback.answer()


@router_client.callback_query(F.data == 'Ресурсы ВятГУ')
async def source_vyatsu(callback: CallbackQuery):
    await update_BD(callback, "Ресурсы ВятГУ")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сайт ВятГУ', url='https://www.vyatsu.ru/'),
         InlineKeyboardButton(text='Личный кабинет', url='https://new.vyatsu.ru/account/')],
        [InlineKeyboardButton(text='Moodle', url='https://e.vyatsu.ru/'),
         InlineKeyboardButton(text='VK', url='https://vk.com/vyatsu')],
        [InlineKeyboardButton(text='Telegram', url='https://t.me/vyatsunews')],
        [InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])
    await callback.message.edit_text("Ресурсы ВятГУ", reply_markup=keyboard)
    await callback.answer()


@router_client.callback_query(F.data == 'Цифровые кафедры')
async def digital_departments(callback: CallbackQuery):
    await update_BD(callback, "Цифровые кафедры")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1 модуль', callback_data='1 модуль'),
         InlineKeyboardButton(text='2 модуль', callback_data='2 модуль'),
         InlineKeyboardButton(text='3 модуль', callback_data='3 модуль'),
         InlineKeyboardButton(text='4 модуль', callback_data='4 модуль')],
        [InlineKeyboardButton(text='5 модуль', callback_data='5 модуль'),
         InlineKeyboardButton(text='6 модуль', callback_data='6 модуль'),
         InlineKeyboardButton(text='7 модуль', callback_data='7 модуль'),
         InlineKeyboardButton(text='8 модуль', callback_data='8 модуль')],
        [InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])
    await callback.message.edit_text("1 модуль - основы программирования на Python\n2 модуль - основы алгоритмизации\n3 модуль - базы данных и реляционная алгебра\n4 модуль - cтандартные библиотеки Python\n5 модуль - моделирование бизнес-процессов\n6 модуль - разработка баз данных\n7.1 модуль - анализ данных\n7.2 модуль - UI/UX-дизайн\n7.3 модуль - Основы веб-разработки\n8 модуль - практика в профильной сфере", reply_markup=keyboard)
    await callback.answer()