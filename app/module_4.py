from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_4 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции4'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ4')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами4')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_4.callback_query(F.data == '4 модуль')
async def module_4(callback: CallbackQuery):
    await update_BD(callback, "4 модуль")
    await callback.message.edit_text("Модуль 4", reply_markup=keyboard)
    await callback.answer()


@router_module_4.callback_query(F.data == 'Файл со всеми материалами4')
async def file_4(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами4")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7zGT_NahmIErIaLv1v9hRf5iAhh5SAAJ2OAAC3_T4S8G13Su5bMKlMAQ")
        await callback.message.answer("Модуль 4", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/MMkW9IKBqjo'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 41')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/aIJWHeepO7s'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 42')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/pEvhS_YPjaI'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 43')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/hW4CFDfKSNA'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 44')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/lt7QdWC-Wfw'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 45')],
    [InlineKeyboardButton(text='Назад', callback_data='4 модуль')]
    ])


@router_module_4.callback_query(F.data == 'Лекции4')
async def lect_4(callback: CallbackQuery):
    await update_BD(callback, "Лекции4")
    await callback.message.edit_text("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_4.callback_query(F.data == 'Материал 41')
async def material_41(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7zmT_NiQhOI-3WTNZZiffYYAYU5FEAAKCOAAC3_T4Sz_JX0W2wiHVMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI70GT_Nifa-C2d_3wm16exysb64gTPAAKEOAAC3_T4S9TGTYvAz_2RMAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_4.callback_query(F.data == 'Материал 42')
async def material_42(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI70mT_Nk4bZY_oDQqSjsBF5mdLiOngAAKJOAAC3_T4S7gyHEgLJD1bMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI71GT_NlR4QUWkWw4zMwcGY8j4wm7eAAKLOAAC3_T4S-R2pueV_vCyMAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Материал 43')
async def material_43(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI71mT_Nn38vcCO8u3d3oi0RSb-hw_OAAKPOAAC3_T4S9e1FSLLGH3SMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI72GT_NoAtdZc6nM9Jsgbo0CSGw7tcAAKQOAAC3_T4S6PnAZa9dBWUMAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Материал 44')
async def material_44(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI72mT_NqnXAAH2E0eqY0Utng_xGjZLtgAClzgAAt_0-EvotVRgyYq5WzAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI73GT_Nq890UYP2CpU9--iHqIwQuPaAAKZOAAC3_T4S8iApDPpJvObMAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Материал 45')
async def material_45(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI73mT_NtZk0KlixnO2rN889rwueC3FAAKfOAAC3_T4S5xMkRJcw1r4MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI74GT_Ntk5eNH4sZG9hAdFb9KFXWGjAAKgOAAC3_T4S8Orf3vnmr9LMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI74mT_Nt10EAiBNnOrrBBDfOfjug2RAAKiOAAC3_T4Sz9UuHMwtfurMAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 41')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 42')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 43')],
    [InlineKeyboardButton(text='Назад', callback_data='4 модуль')]
    ])


@router_module_4.callback_query(F.data == 'Материал лаб. работ4')
async def lect_4(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ4")
    await callback.message.edit_text("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_4.callback_query(F.data == 'Лабораторная работа 41')
async def lab_41(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI7_mT_N4GbrSSICVmhHlSglgv6YzPIAAKzOAAC3_T4S32xjTENXZBFMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8AAFk_zeF_hJUs7pjY_kI17SswFqlbgACtTgAAt_0-EvYSbZSvw3QRDAE")
        await callback.message.answer("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_4.callback_query(F.data == 'Лабораторная работа 42')
async def lab_42(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8AmT_N7JU37z8RBRcZrgPuZ1Jd_ypAAK7OAAC3_T4SxMPSEGAhahLMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8BGT_N7YhB9yAjrZ33qg-FY-KLmNYAAK8OAAC3_T4S48fOAGkCAOmMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8BmT_N7kn-vMhQyxHdGEK8-T6JegzAAK9OAAC3_T4S9_ohQ6YPqQ6MAQ")
        await callback.message.answer("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Лабораторная работа 43')
async def lab_43(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8CGT_N-s8v--QU-k-DmcI-CQif2cNAALFOAAC3_T4SxZ3DfKpTqnSMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8CmT_N-1TN4TDYt_LKSo_nFGarJ3CAALGOAAC3_T4Sz8UT2Cafr5MMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8DGT_N_F7mwuxCEpnOu1peugVeXnhAALIOAAC3_T4S0WkNUuKhAOFMAQ")
        await callback.message.answer("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
        await callback.answer()