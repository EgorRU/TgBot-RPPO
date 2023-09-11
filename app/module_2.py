from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_2 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции2'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ2')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами2')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_2.callback_query(F.data == '2 модуль')
async def module_2(callback: CallbackQuery):
    await update_BD(callback, "2 модуль")
    await callback.message.edit_text("Модуль 2", reply_markup=keyboard)
    await callback.answer()


@router_module_2.callback_query(F.data == 'Файл со всеми материалами2')
async def file_2(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами2")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7B2T_LgRf1S8eD2ANQ2H2zasOL41uAAKSNwAC3_T4S3_9U9BLO1Q1MAQ")
        await callback.message.answer("Модуль 2", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/b2uPoHBWEhE'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 21')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/h7Z31Okj6tY?list=PLjQrQCcomcyN2UWgeg2IF7LnYwoUMPYXj'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 22')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/j_pq-0v1S1s?list=PLjQrQCcomcyN2UWgeg2IF7LnYwoUMPYXj'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 23')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/2GL8TERJ_zg?list=PLjQrQCcomcyN2UWgeg2IF7LnYwoUMPYXj'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 24')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/yughW7TL8gY'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 25')],
    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
    ])


@router_module_2.callback_query(F.data == 'Лекции2')
async def lect_2(callback: CallbackQuery):
    await update_BD(callback, "Лекции2")
    await callback.message.edit_text("Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_2.callback_query(F.data == 'Материал 21')
async def material_21(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7D2T_LrXP1BWy6qMtXmKbmZ4pcstUAAKlNwAC3_T4SymDsQU81XdoMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7EWT_LrlIQix_aHkGbM4Hxiq2ZhwcAAKnNwAC3_T4SwNl5sqN44cvMAQ")
        await callback.message.answer("Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_2.callback_query(F.data == 'Материал 22')
async def material_22(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7E2T_LwABgJwmdLP7tJIIdmiriaxTTwACsTcAAt_0-EtPX2yPart8MDAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7FWT_LwR6wB6D0RFiE4hMulNyWc_KAAKyNwAC3_T4SzcCEKcIw2JaMAQ")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Материал 23')
async def material_23(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7IWT_L1kzBduD3YyDEZScCKebFcjAAALBNwAC3_T4S8Dc9NQDySbaMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7I2T_L13OsHtUhJmBwtI2A2y0TDvSAALCNwAC3_T4Szus5IbOLP2IMAQ")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Материал 24')
async def material_24(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7J2T_L44SUF7wUBoi4h7WqvGZpU5yAALHNwAC3_T4S7IMPVOIYsKyMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7KWT_L5bWxU8jfvqYZ7Ew7FBu8TJ-AALINwAC3_T4SxCxFEautkfCMAQ")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Материал 25')
async def material_25(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7K2T_L_Od-M7vVsS5rVJskcBa8AABTAACzTcAAt_0-EuqjZ0LNzdc9DAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7LWT_L_fD10D93GeuxeHXEEpXx4TfAALONwAC3_T4S_K_njNTxoDfMAQ")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 21')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 22')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 23')],
    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
    ])


@router_module_2.callback_query(F.data == 'Материал лаб. работ2')
async def lect_2(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ2")
    await callback.message.edit_text("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_2.callback_query(F.data == 'Лабораторная работа 21')
async def lab_21(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7RWT_MGNbVP1pULGfO7Fvwi2-zXv5AALVNwAC3_T4S0ves-AjeRuqMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7R2T_MGSxfRj5spVe_FAaYkUIIjdAAALWNwAC3_T4S126UzAbLWkfMAQ")
        await callback.message.answer("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_2.callback_query(F.data == 'Лабораторная работа 22')
async def lab_22(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7SWT_MI49Og4Vedq4fGdnqi8L3TKjAALaNwAC3_T4S1R_SQb24aVIMAQ")
        await callback.message.answer("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Лабораторная работа 23')
async def lab_23(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7S2T_MLVsgaSXHS3nonwKkdtdGDQuAALcNwAC3_T4SxHzmrHnvruXMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7TWT_MLeDHw0bWODOvHj607dyuinlAALfNwAC3_T4S2rNdZ1rWHjSMAQ")
        await callback.message.answer("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
        await callback.answer()