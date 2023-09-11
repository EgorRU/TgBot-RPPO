from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_6 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции6'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ6')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами6')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_6.callback_query(F.data == '6 модуль')
async def module_6(callback: CallbackQuery):
    await update_BD(callback, "6 модуль")
    await callback.message.edit_text("Модуль 6", reply_markup=keyboard)
    await callback.answer()


@router_module_6.callback_query(F.data == 'Файл со всеми материалами6')
async def file_6(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами6")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8d2T_O_zuyT3GjAABrN6rhhlUM54HAANJOQAC3_T4S3jMry4pKZ6dMAQ")
        await callback.message.answer("Модуль 6", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/dfIqseL0jVU'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 61')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/GQNOQ15gqyo'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 62')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/IZK7Xga7Rl8'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 63')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/MJY3-_OxvrM'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 64')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/TgKv1trj8Cc'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 65')],
    [InlineKeyboardButton(text='Назад', callback_data='6 модуль')]
    ])


@router_module_6.callback_query(F.data == 'Лекции6')
async def lect_6(callback: CallbackQuery):
    await update_BD(callback, "Лекции6")
    await callback.message.edit_text("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_6.callback_query(F.data == 'Материал 61')
async def material_61(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8gmT_PKPXw1eqyz8UE-ewB7o4_z7VAAJbOQAC3_T4S1bFzwpfAAGiVjAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8g2T_PKOEjiO1VGJ8jXKEb5G1LC2xAAJcOQAC3_T4S2_OETiUSdgAATAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8hmT_PKk7BSwse9unk7ZDtyWuvoOhAAJeOQAC3_T4S00aC74TmBeVMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_6.callback_query(F.data == 'Материал 62')
async def material_62(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8iGT_PNaXi3JX-jC-a6kFhol-u98wAAJlOQAC3_T4SztOta1VLpmSMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8iWT_PNZz2FNe_x4gLAcMGgMi_DsqAAJmOQAC3_T4SzXM3eVDF2A2MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8jGT_PNo-hh7Mnna83_7IxHY4cK8GAAJoOQAC3_T4S9FCK0wh41I9MAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Материал 63')
async def material_63(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8jmT_PQbZWAJTsVEBfR42Qec21c8rAAJtOQAC3_T4S4WeSKwVTQHpMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8kGT_PQyZEfiMrNI_MTDJUTMBX5FiAAJuOQAC3_T4SyenaGmJLKFwMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Материал 64')
async def material_64(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8kmT_PTA8jbWs4aMhAAFvtlMQ8EU_ZAACcDkAAt_0-Eu2HutMGt_p5zAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8lGT_PTNJgK1PZMnYe2QcimsViM_1AAJxOQAC3_T4S68bcM8Rv7NiMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Материал 65')
async def material_65(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8lmT_PVdbWzoOucD1gEWUoR0QAVv0AAJzOQAC3_T4S-qwKtnLKBgfMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8mGT_PVmVdbAMKTOJK0M6nEZZP_PIAAJ0OQAC3_T4SwbWpuO8LGTrMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 61')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 62')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 63')],
    [InlineKeyboardButton(text='Назад', callback_data='6 модуль')]
    ])


@router_module_6.callback_query(F.data == 'Материал лаб. работ6')
async def lect_6(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ6")
    await callback.message.edit_text("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_6.callback_query(F.data == 'Лабораторная работа 61')
async def lab_61(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8mmT_PZMeJKGq6EsoHYIbOTmVzXroAAJ5OQAC3_T4S_XBJhNkaI09MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8nGT_PZW-0tkefKKUIc45LK6wE63sAAJ6OQAC3_T4S1Tnw9orYKLaMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8nmT_PZcHK-ISqPsWGEQhjbeYXwcrAAJ7OQAC3_T4S67nRDIVImjEMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8oGT_PZrnl373wdjn3XaiIqHaVkmGAAJ8OQAC3_T4SzhnI9fLZxjcMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8omT_PZ7chJVHuovMH0I-PK5CY1J7AAJ9OQAC3_T4S-FGcxRm7d16MAQ")
        await callback.message.answer("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_6.callback_query(F.data == 'Лабораторная работа 62')
async def lab_62(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8pGT_PeT7SEyaEPvoUIh7_mlEHyZmAAKGOQAC3_T4SwXXuuDpwabyMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8pmT_PeVYJDwKQOFKcp2Hp_g_l3R9AAKHOQAC3_T4S5zKRqUSTafnMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8qGT_PenIms54sJjPPpGUIiKyxsqaAAKIOQAC3_T4Sz-HiYdaqizFMAQ")
        await callback.message.answer("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Лабораторная работа 63')
async def lab_63(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8qmT_PhBvBh2m92UsUiZ7VyBlpMQEAAKKOQAC3_T4SwTD0rHsRMPVMAQ")
        await callback.message.answer("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
        await callback.answer()