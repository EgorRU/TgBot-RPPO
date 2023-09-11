from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_5 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции5'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ5')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами5')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_5.callback_query(F.data == '5 модуль')
async def module_5(callback: CallbackQuery):
    await update_BD(callback, "5 модуль")
    await callback.message.edit_text("Модуль 5", reply_markup=keyboard)
    await callback.answer()


@router_module_5.callback_query(F.data == 'Файл со всеми материалами5')
async def file_5(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами5")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8I2T_OLjHgQ1tUmgcydEkUhLeJO7wAALXOAAC3_T4S1qdnixqa9k2MAQ")
        await callback.message.answer("Модуль 5", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/DI2OyecP8dA'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 51')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/JIslvRvDj0A'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 52')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/JIslvRvDj0A'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 53')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/iL1LuiwUeQA'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 54')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/-SoKsuCA4Lk'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 55')],
    [InlineKeyboardButton(text='Назад', callback_data='5 модуль')]
    ])


@router_module_5.callback_query(F.data == 'Лекции5')
async def lect_5(callback: CallbackQuery):
    await update_BD(callback, "Лекции5")
    await callback.message.edit_text("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_5.callback_query(F.data == 'Материал 51')
async def material_51(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8LmT_OYoQNvZr2aQ_iay0RMIUFn6SAALzOAAC3_T4S_AkSN_J6EAhMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8MGT_OYxqe488g4yDTzyX7v9ZaRpKAAL0OAAC3_T4S2w3LlzIpqvsMAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_5.callback_query(F.data == 'Материал 52')
async def material_52(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8MmT_ObYKBc71AAGHcj847xrcodWjcwAC-jgAAt_0-EtUWCe1QVrogjAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8NGT_ObxMc0YKjgYB7L5rmJExmpEOAAL7OAAC3_T4S-Y9iDx7-aVvMAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Материал 53')
async def material_53(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8NmT_OhRm2jeip4IQuP8-yW4WkLxaAAIDOQAC3_T4S5pqXUMJnpIuMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8OGT_OhdJDZxPmgABMKVNJJtyjp0h5gACBjkAAt_0-EtoDrNPlJ5SgjAE")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Материал 54')
async def material_54(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8OmT_OjqFR-WYXO0vIc8nHXGdsP3BAAILOQAC3_T4S_C_ydiLRDudMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8PGT_OjwfreMV3IoD3YV0RPWz9gABkQACDDkAAt_0-Evz2DeSAlAMNDAE")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Материал 55')
async def material_55(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8PmT_Ol3G7hr_MMEw94Y38WxxUdxEAAIUOQAC3_T4S4GIUb5NLGVMMAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 51')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 52')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 53')],
    [InlineKeyboardButton(text='Назад', callback_data='5 модуль')]
    ])


@router_module_5.callback_query(F.data == 'Материал лаб. работ5')
async def lect_5(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ5")
    await callback.message.edit_text("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_5.callback_query(F.data == 'Лабораторная работа 51')
async def lab_51(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8WGT_Os_Di85xLPjADH2g-TDRVTOeAAIhOQAC3_T4SyiRlgLFriTeMAQ")
        await callback.message.answer("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_5.callback_query(F.data == 'Лабораторная работа 52')
async def lab_52(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8XGT_OvBV1GwWB2G07_oictpeeEQcAAIkOQAC3_T4Sx0dT6VhZ3MgMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8WmT_OushIBMGCag499IryR_TGhEKAAIjOQAC3_T4S6fXAAFsrcdmNjAE")
        await callback.message.answer("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Лабораторная работа 53')
async def lab_53(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8XmT_OxFXA37DjId0A4C5qQABjD4hdwACKTkAAt_0-EvfwpX31fj5TzAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8YGT_OxL2f4VtJKnGJOTqM5p3I56kAAIqOQAC3_T4S_r6FLwEXWgiMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8YmT_OxhhtBHz5QWJ17DSEwlYlWptAAIsOQAC3_T4S0hPh2YTegI1MAQ")
        await callback.message.answer("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
        await callback.answer()