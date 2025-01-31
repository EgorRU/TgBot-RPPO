from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_7_2 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7_2'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7_2')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ7_2'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал7_2')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами7_2'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')]
])

message_text = '7.2 модуль - UI/UX-дизайн'


@router_module_7_2.callback_query(F.data == '7_2 модуль')
async def module_7_2(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()
