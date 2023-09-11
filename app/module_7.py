from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_7 = Router()


keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Анализ данных', callback_data='7.1 модуль')],
    [InlineKeyboardButton(text='UI/UX-дизайн', callback_data='7.2 модуль')],
    [InlineKeyboardButton(text='Основы веб-разработки', callback_data='7.3 модуль')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры')]
    ])


@router_module_7.callback_query(F.data == '7 модуль')
async def module_7_main(callback: CallbackQuery):
    await update_BD(callback, "7 модуль")
    await callback.message.edit_text("Модуль 7", reply_markup=keyboard_main)
    await callback.answer()
    

keyboard7_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7.1'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7.1')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами7.1')],
    [InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=640129')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


keyboard7_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7.2'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7.2')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами7.2')],
    [InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=640457')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


keyboard7_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7.3'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7.3')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами7.3')],
    [InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=640589')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


@router_module_7.callback_query(F.data == '7.1 модуль')
async def module_7_1(callback: CallbackQuery):
    await update_BD(callback, "Анализ данных")
    await callback.message.edit_text("Модуль 7.1", reply_markup=keyboard7_1)
    await callback.answer()
    

@router_module_7.callback_query(F.data == '7.2 модуль')
async def module_7_2(callback: CallbackQuery):
    await update_BD(callback, "UI/UX-дизайн")
    await callback.message.edit_text("Модуль 7.2", reply_markup=keyboard7_2)
    await callback.answer()
    

@router_module_7.callback_query(F.data == '7.3 модуль')
async def module_7_3(callback: CallbackQuery):
    await update_BD(callback, "Основы веб-разработки")
    await callback.message.edit_text("Модуль 7.3", reply_markup=keyboard7_3)
    await callback.answer()


@router_module_7.callback_query(F.data == 'Файл со всеми материалами7.1')
async def file_7_1(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами7.1")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI81mT_QBwzOYWkxekG-gscdE-kkomYAAKbOQAC3_T4S19OgQyXHgYXMAQ")
        await callback.message.answer("Модуль 7.1", reply_markup=keyboard7_1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Файл со всеми материалами7.2')
async def file_7_2(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами7.2")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI84mT_QUBaMdK3MZOTZ5OlDFe5d3xOAAK3OQAC3_T4S54bAWZ9QxxPMAQ")
        await callback.message.answer("Модуль 7.2", reply_markup=keyboard7_2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Файл со всеми материалами7.3')
async def file_7_3(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами7.3")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI85GT_QU9Ip4GkotNLwinjYYHQum3qAAK4OQAC3_T4S1drYwpWaK87MAQ")
        await callback.message.answer("Модуль 7.3", reply_markup=keyboard7_3)
        await callback.answer()


keyboard_lecture1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/ZHpMUlr5pyA'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 71_1')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/KWlWJkSMByQ'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 71_2')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/G7IuOrpNZiw'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 71_3')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/A-SG4-r6igA'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 71_4')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/-5Q5duCKYIQ'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 71_5')],
    [InlineKeyboardButton(text='Назад', callback_data='7.1 модуль')]
    ])


keyboard_lecture2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/QvkIIGe3kso'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 72_1')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/G5_gGq4Ohu8'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 72_2')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/B5pUrmvyY8M'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 72_3')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/-TYHnF5DX0M'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 72_4')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/qlrMLGx276s'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 72_5')],
    [InlineKeyboardButton(text='Назад', callback_data='7.2 модуль')]
    ])


keyboard_lecture3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/iT7DX8ZQcgM'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 73_1')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/D0M1T3ao1DA'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 73_2')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/4PZMPD8AKBE'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 73_3')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/sNWlPgMB-DY'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 73_4')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/GtGvdIM7Aqk'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 73_5')],
    [InlineKeyboardButton(text='Назад', callback_data='7.3 модуль')]
    ])


@router_module_7.callback_query(F.data == 'Лекции7.1')
async def lect_7_1(callback: CallbackQuery):
    await update_BD(callback, "Лекции7.1")
    await callback.message.edit_text("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Лекции7.2')
async def lect_7_2(callback: CallbackQuery):
    await update_BD(callback, "Лекции7.2")
    await callback.message.edit_text("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Лекции7.3')
async def lect_7_3(callback: CallbackQuery):
    await update_BD(callback, "Лекции7.3")
    await callback.message.edit_text("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
    await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 71_1')
async def material_71_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8-WT_RTy-aqw7rDgQvt0a9-TncFdNAALOOQAC3_T4Sy6kg2-Vk15XMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8-2T_RT6Q1Cn7zq-CCGeDYRZc_KU1AALPOQAC3_T4S9bgXjjzzHCJMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 71_2')
async def material_71_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8_WT_RWCsmowlZiGAtLR8S_lM0bTTAALROQAC3_T4S7Md6Jh2mTiTMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 71_3')
async def material_71_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI8_2T_RYUMQdKSyYq2brvBOb40sPC3AALTOQAC3_T4SwNu81FXE2KBMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 71_4')
async def material_71_4(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9AWT_RZ43mgdfP2ElNckWEe2l4AOYAALUOQAC3_T4Sx-alOwN3zVgMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 71_5')
async def material_71_5(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9A2T_Rbts5CA4B5CoSzsAASYCU1p1eQAC1jkAAt_0-EuuJiJzV4DobTAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9BWT_Rb63MbQjUaO9feof3-7N1mLMAALXOQAC3_T4S_YhfL0qQkLyMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 72_1')
async def material_72_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9B2T_RfIItmizzDQAARdgLO2RLWS27wAC2zkAAt_0-EvZQNigsgXDKTAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9CWT_RfND3KHgHqZ6Mz5p6Y1cSYDJAALcOQAC3_T4S3Xwd8OHNisHMAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 72_2')
async def material_72_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9C2T_RhUMvgjUucTL1aGy5b8Dv59jAALfOQAC3_T4S-XrPGJATw9XMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9DWT_Rhdmlvuq7a8RFXS66V2eh369AALgOQAC3_T4S8dWAj2vaG67MAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 72_3')
async def material_72_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9D2T_Rjex95WDrxv8t4ZthfxvCNI5AALiOQAC3_T4Sx-MgjAurlvcMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9EWT_RjlxF-pp6Kwc0GdSLkDzg3WrAALjOQAC3_T4Sx92OZWr8o6yMAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 72_4')
async def material_72_4(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9E2T_Rli2LV_Jjm06gbfSnWmUtERMAALlOQAC3_T4S4Xya3XHW3gnMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9FWT_Rl7VPnWPaEoMmFLQ6-QX6G7oAALmOQAC3_T4S6lM0k2XneAlMAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 72_5')
async def material_72_5(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9F2T_RnqkKBYVb8SHc5doUaFi6NU9AALnOQAC3_T4S1lVn8rgX7zFMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9GWT_RnzrL5-YQWNfvFwHD8UE4x6KAALoOQAC3_T4S0qh8qG20LDxMAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_1')
async def material_73_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9G2T_RqAKC8JNHuYKV2MOx9QE1HtfAALpOQAC3_T4S8LMd_i6l5BpMAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 73_2')
async def material_73_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9HWT_Rra-OcIWogj6YZrKhGeIfd71AALqOQAC3_T4SzhVT68oluYyMAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_3')
async def material_73_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9H2T_Rs7QBYdZVWy2H9WwqYuEb9SgAALuOQAC3_T4Sxm1N58eaXqAMAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_4')
async def material_73_4(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9IWT_RubpZGe2oberoPcxJN68yZTjAALwOQAC3_T4S9Q1aEVCDu5XMAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_5')
async def material_73_5(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9I2T_Rv7TXmo4WRh66thNyCIFn8-TAALzOQAC3_T4S-tCKprCbrWuMAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

keyboard_labs1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 71_1')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 71_2')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 71_3')],
    [InlineKeyboardButton(text='Назад', callback_data='7.1 модуль')]
    ])


keyboard_labs2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 72_1')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 72_2')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 72_3')],
    [InlineKeyboardButton(text='Назад', callback_data='7.2 модуль')]
    ])


keyboard_labs3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 73_1')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 73_2')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 73_3')],
    [InlineKeyboardButton(text='Назад', callback_data='7.3 модуль')]
    ])


@router_module_7.callback_query(F.data == 'Материал лаб. работ7.1')
async def lect_71(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ7.1")
    await callback.message.edit_text("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Материал лаб. работ7.2')
async def lect_72(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ7.2")
    await callback.message.edit_text("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Материал лаб. работ7.3')
async def lect_73(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ7.3")
    await callback.message.edit_text("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
    await callback.answer()
    
   
@router_module_7.callback_query(F.data == 'Лабораторная работа 71_1')
async def lab_71_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9cmT_Sn9Jy8D3nRMgvwRmWPuxo72SAAIgOgAC3_T4S4NxCWMOwx-2MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9dGT_SoP2aOz01C7LbBneW5almmPbAAIhOgAC3_T4S218yupg8grrMAQ")
        await callback.message.answer("https://youtu.be/djuHlDYccCU")
        await callback.message.answer("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Лабораторная работа 71_2')
async def lab_71_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9dmT_Srlu728PS-I2a5cDp9DjY76MAAImOgAC3_T4S4Zs7YiLzYOZMAQ")
        await callback.message.answer("https://youtu.be/p_jBR4y351g")
        await callback.message.answer("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 71_3')
async def lab_71_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9eGT_SvJvebZvgYLYDxMUMK0a7UulAAIvOgAC3_T4S1XpYUtFZDnlMAQ")
        await callback.message.answer("https://youtu.be/ut2GMNxxpC4")
        await callback.message.answer("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 72_1')
async def lab_72_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9emT_Sy4kkvQx29tIl8bK8_LNTc1AAAIxOgAC3_T4SwSGzvIotT9DMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9fGT_S3nZ0xjJLlb0vDBDSyA24xlhAAI3OgAC3_T4S5zSjRQwMNuaMAQ")
        await callback.message.answer("https://youtu.be/mzZMdc-jLqQ")
        await callback.message.answer("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Лабораторная работа 72_2')
async def lab_72_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9qmT_TS5g6lMUVjk1Fjer4O86-TAtAAJOOgAC3_T4S0ddhrZKkLoEMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9qGT_TSqYkpAYoVnp7LuUeGYIPWTnAAJNOgAC3_T4S6KuWulvgKxzMAQ")
        await callback.message.answer("https://youtu.be/mOYpukKC-Uc")
        await callback.message.answer("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 72_3')
async def lab_72_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9gmT_S8lFyQfujfOv5CKzVGK416IzAAI_OgAC3_T4S1Phzzx8ZbomMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9hGT_S9cpMsJYyGOQWEMQ7JXDlD-yAAJAOgAC3_T4S8LVcyrDDYYuMAQ")
        await callback.message.answer("https://youtu.be/Q14Rc_QsEUE")
        await callback.message.answer("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 73_1')
async def lab_73_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9hmT_TDvCDTLihG6LzOPeJ_IE_AjVAAJCOgAC3_T4S6_26fhzgRIsMAQ")
        await callback.message.answer("https://youtu.be/afUQcFZOYfY")
        await callback.message.answer("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Лабораторная работа 73_2')
async def lab_73_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9iGT_TFdUasPXvX7K2i69c8D0RisvAAJFOgAC3_T4Sy5YRFW3eafdMAQ")
        await callback.message.answer("https://youtu.be/T-Kvj3ibRjM")
        await callback.message.answer("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 73_3')
async def lab_73_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI9imT_THW0NdLecxeLyVS6mM1VhT1DAAJHOgAC3_T4S5i4h04jgO7GMAQ")
        await callback.message.answer("https://youtu.be/hY7QRLHvl0Q")
        await callback.message.answer("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
        await callback.answer()