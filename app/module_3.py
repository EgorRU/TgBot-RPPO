from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_3 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции3'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ3')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами3')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_3.callback_query(F.data == '3 модуль')
async def module_3(callback: CallbackQuery):
    await update_BD(callback, "3 модуль")
    await callback.message.edit_text("Модуль 3", reply_markup=keyboard)
    await callback.answer()


@router_module_3.callback_query(F.data == 'Файл со всеми материалами3')
async def file_3(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами3")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7cGT_MlwYfFL8lvK3HjkVot4iUSJdAAL4NwAC3_T4S3ipv8cPuhthMAQ")
        await callback.message.answer("Модуль 3", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/DqaFNejpA1c'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 31')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/ViBLgHyxsHI'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 32')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/-WNZte7Rgn4'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 33')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/bdt9ffXfn3c'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 34')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/VvSVLJovQR8'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 35')],
    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
    ])


@router_module_3.callback_query(F.data == 'Лекции3')
async def lect_3(callback: CallbackQuery):
    await update_BD(callback, "Лекции3")
    await callback.message.edit_text("Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_3.callback_query(F.data == 'Материал 31')
async def material_31(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7cmT_Ms75pHIG0-6RYE4Pk1Aa-KafAAIKOAAC3_T4S_blrno6MLEOMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7dGT_Ms9NhnDR0gXqpar9OfgfmE2aAAILOAAC3_T4S-ZBqrXPfz6SMAQ")
        await callback.message.answer("Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_3.callback_query(F.data == 'Материал 32')
async def material_32(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7dmT_MyCQZncee04Y0pnG49VcHXM4AAIWOAAC3_T4S4Y7auasw1ctMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7eGT_MyIvQolL7ZszG-KNg2r1ORBtAAIXOAAC3_T4S9LxE3pxO0g7MAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Материал 33')
async def material_33(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7emT_M0VTDwABj1TyHvWepLtn-3gtGgACHDgAAt_0-EvHswABCZSWeD4wBA")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7fGT_M0panMZdPplwUzDCaXdvWsL4AAIeOAAC3_T4S0GXHmXrO4jbMAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Материал 34')
async def material_34(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7gGT_M3nOY88g4XbCcS8PoCFaQnP0AAIjOAAC3_T4S8d8puF5Cx93MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7gmT_M3sWarfA1cxh2JspQfyafPaRAAIkOAAC3_T4S2on0uU3VVwxMAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Материал 35')
async def material_35(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7hGT_M6HF38n1G_xHfxMX_ohmQgABsQACJzgAAt_0-EvmOpXwCtgCBzAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7hmT_M6P5DDyklZ96PC7lArDopiAuAAIpOAAC3_T4Sw-n6ME0ZKWcMAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 31')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 32')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 33')],
    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
    ])


@router_module_3.callback_query(F.data == 'Материал лаб. работ3')
async def lect_3(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ3")
    await callback.message.edit_text("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_3.callback_query(F.data == 'Лабораторная работа 31')
async def lab_31(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7oWT_NEnuVqqAgkrAR68M8HF4bZuqAAJBOAAC3_T4SzmsBGELJL6YMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7omT_NEms-2Ku6Vtzhm0XLaMftvn7AAJCOAAC3_T4S0WUoBMm_FWpMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7pWT_NFJi8uxKXePkmz5g2QuVPtSRAAJEOAAC3_T4S0RPE1IDM5AjMAQ")
        await callback.message.answer("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_3.callback_query(F.data == 'Лабораторная работа 32')
async def lab_32(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7p2T_NHZJQL8IT1Or-W4t_8Pz4alGAAJJOAAC3_T4SxPoUnl54I9qMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7qWT_NHgY5EqiCYhgy3rsezqsHB-AAAJKOAAC3_T4S_TcyvoIoZUvMAQ")
        await callback.message.answer("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Лабораторная работа 33')
async def lab_33(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7q2T_NKWwb9-c7oKAhgGQOB1TG7sSAAJNOAAC3_T4S0w0HNNUfEydMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7rWT_NKlIUbzNtZk6xxfSR-k-7Rk1AAJPOAAC3_T4S_ekkq6eL861MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7r2T_NK92Ni-3iQsocrAvtbR4TErdAAJROAAC3_T4Swl5Yu-Ji26GMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7sWT_NLMWw8neIHCXlXPPnA-zZuQhAAJTOAAC3_T4S2jSMD0N6EpVMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7s2T_NLqQAdnjiPOIu1IGL0yVjR5rAAJUOAAC3_T4S0F73ZvbfZDsMAQ")
        await callback.message.answer("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
        await callback.answer()