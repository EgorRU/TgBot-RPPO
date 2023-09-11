from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_1 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции1'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ1')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами1')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_1.callback_query(F.data == '1 модуль')
async def module_1(callback: CallbackQuery):
    await update_BD(callback, "1 модуль")
    await callback.message.edit_text("Модуль 1", reply_markup=keyboard)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Файл со всеми материалами1')
async def file_1(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами1")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6UmT_JMu5J6ZNmrzusnimMLYFMNmZAAIKNwACf_H4S1DbaO_gPXlgMAQ")
        await callback.message.answer("Модуль 1", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/FK-sqG2mrlk'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 11')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/1fJ3LFlWY3I'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 12')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/eJRZwVaix9s'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 13')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/GP0jUYaZBHs'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 14')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/cQ7_4Lg99sw'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 15')],
    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
    ])


@router_module_1.callback_query(F.data == 'Лекции1')
async def lect_1(callback: CallbackQuery):
    await update_BD(callback, "Лекции1")
    await callback.message.edit_text("Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Материал 11')
async def material_11(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6ZWT_J9T6fCm7-kai7Bpf7Y_33RLyAAIQNwAC3_T4SzteZuCuWelNMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6Z2T_J-2cSNDOptIFX2-XGyMq3ejeAAIRNwAC3_T4S2wJCHJ6CWRNMAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_1.callback_query(F.data == 'Материал 12')
async def material_12(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6gWT_KSq3oYVcZOJ9atMm0RihjzQbAAIkNwAC3_T4S_ePeXM5m6UKMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6e2T_KSKPg0jhe0AneHH4QAKSw3tWAAIjNwAC3_T4SzoOhSG9LT1_MAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 13')
async def material_13(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6g2T_KXDX9c8XNDAHLAJNc5zZjDr9AAIsNwAC3_T4S2SFwCHUw9GiMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6hWT_KXNKthL9B3HA5a3caZme2c89AAIuNwAC3_T4S4VHi8mD1VVhMAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 14')
async def material_14(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6lWT_KdqJJY7MXlwiguqgmNV94421AAI1NwAC3_T4S-ekDWzTuTCPMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6l2T_KdxTSpx1YBEJBZ7G68f4zdAuAAI2NwAC3_T4S2gH3CQU48LJMAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 15')
async def material_15(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6mWT_Kf4ZD_olwo-ig-gSfRr9Ck7tAAI6NwAC3_T4Sz-F4M5dE0uaMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6m2T_KgOqLm2u6p8E1TDcvJOryV15AAI7NwAC3_T4S0hYDN_nPpI9MAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 11')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 12')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 13')],
    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
    ])


@router_module_1.callback_query(F.data == 'Материал лаб. работ1')
async def lect_1(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ1")
    await callback.message.edit_text("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_1.callback_query(F.data == 'Лабораторная работа 11')
async def lab_11(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6vWT_K8UNlaNSjFB8NYjVTVh53qoYAAJhNwAC3_T4S1Z3gDsXi7OqMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6v2T_K8jdb7V5CzYdRNuBag4UO46lAAJiNwAC3_T4S-iE07nbhPKhMAQ")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_1.callback_query(F.data == 'Лабораторная работа 12')
async def lab_12(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6wWT_LAinTIC67t5vtRfss-W36i12AAJpNwAC3_T4S15mhaOIRGMAATAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6w2T_LA7YtuvyTF4Pa2xtbLXFtf5zAAJrNwAC3_T4S8mb80_uihocMAQ")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Лабораторная работа 13')
async def lab_13(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6xWT_LDEGsI784ogzRCs6Hp22wKrLAAJwNwAC3_T4S8_EnqyD4AABzzAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI6x2T_LDbOsOgPKMYwSyD6tZXrfa1tAAJyNwAC3_T4S9wRCPHWb2-9MAQ")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()