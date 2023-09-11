from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_8 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Проект на тему "Анализ данных"', callback_data='Проект на тему "Анализ данных"')],
    [InlineKeyboardButton(text='Проект на тему "UIUX-дизайн"', callback_data='Проект на тему "UIUX-дизайн"')],
    [InlineKeyboardButton(text='Проект на тему "Веб-разработка"', callback_data='Проект на тему "Веб-разработка"')],
    [InlineKeyboardButton(text='Проект на свободную тему', callback_data='Проект на свободную тему')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Консультация', url='https://youtu.be/hO-DE-ZIGl8')],
    [InlineKeyboardButton(text='Методические рекомендации', callback_data='Методические рекомендации1')],
    [InlineKeyboardButton(text='Шаблон отчёта', callback_data='Шаблон отчёта1'),
    InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал1')],
    [InlineKeyboardButton(text='Сдача проекта', url='https://e.vyatsu.ru/mod/assign/view.php?id=641060')],
    [InlineKeyboardButton(text='Назад', callback_data='8 модуль')]
    ])


keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Консультация', url='https://youtu.be/ajcA2SmkwyM')],
    [InlineKeyboardButton(text='Методические рекомендации', callback_data='Методические рекомендации2')],
    [InlineKeyboardButton(text='Шаблон отчёта', callback_data='Шаблон отчёта2'),
    InlineKeyboardButton(text='Доп. материал', url='https://www.figma.com/file/P65xzfVUrAZDGI7txLGgrH/Мой-ВятГУ?type=design&node-id=0%3A1&mode=design&t=p54fv0nRqra2WBvv-1')],
    [InlineKeyboardButton(text='Сдача проекта', url='https://e.vyatsu.ru/mod/assign/view.php?id=641061')],
    [InlineKeyboardButton(text='Назад', callback_data='8 модуль')]
    ])


keyboard3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Консультация', url='https://youtu.be/yTIDS8S3b6M')],
    [InlineKeyboardButton(text='Методические рекомендации', callback_data='Методические рекомендации3')],
    [InlineKeyboardButton(text='Шаблон отчёта', callback_data='Шаблон отчёта3')],
    [InlineKeyboardButton(text='Сдача проекта', url='https://e.vyatsu.ru/mod/assign/view.php?id=641062')],
    [InlineKeyboardButton(text='Назад', callback_data='8 модуль')]
    ])


keyboard4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Консультация', url='https://youtu.be/BkLssvPFttU')],
    [InlineKeyboardButton(text='Методические рекомендации', callback_data='Методические рекомендации4')],
    [InlineKeyboardButton(text='Шаблон отчёта', callback_data='Шаблон отчёта4')],
    [InlineKeyboardButton(text='Сдача проекта', url='https://e.vyatsu.ru/mod/assign/view.php?id=641059')],
    [InlineKeyboardButton(text='Назад', callback_data='8 модуль')]
    ])


@router_module_8.callback_query(F.data == '8 модуль')
async def module_8(callback: CallbackQuery):
    await update_BD(callback, "8 модуль")
    await callback.message.edit_text("Модуль 8", reply_markup=keyboard)
    await callback.answer()


@router_module_8.callback_query(F.data == 'Проект на тему "Анализ данных"')
async def module81(callback: CallbackQuery):
    await callback.message.edit_text("Проект на тему 'Анализ данных'", reply_markup=keyboard1)
    await callback.answer()
    

@router_module_8.callback_query(F.data == 'Проект на тему "UIUX-дизайн"')
async def module82(callback: CallbackQuery):
    await callback.message.edit_text("Проект на тему 'UIUX-дизайн'", reply_markup=keyboard2)
    await callback.answer()
    

@router_module_8.callback_query(F.data == 'Проект на тему "Веб-разработка"')
async def module83(callback: CallbackQuery):
    await callback.message.edit_text('Проект на тему "Веб-разработка"', reply_markup=keyboard3)
    await callback.answer()
    

@router_module_8.callback_query(F.data == 'Проект на свободную тему')
async def module84(callback: CallbackQuery):
    await callback.message.edit_text('Проект на свободную тему', reply_markup=keyboard4)
    await callback.answer()


@router_module_8.callback_query(F.data == 'Методические рекомендации1')
async def method_1(callback: CallbackQuery):
    await update_BD(callback, "Методические рекомендации1")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI92GT_WFJdR0b6XYG7lNnsj5KWShwcAALLOgAC3_T4SxcNApLB_AbEMAQ")
        await callback.message.answer('Проект на тему "Анализ данных"', reply_markup=keyboard1)
        await callback.answer()


@router_module_8.callback_query(F.data == 'Методические рекомендации2')
async def method_2(callback: CallbackQuery):
    await update_BD(callback, "Методические рекомендации2")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI92mT_WKFOk22-y0vp5RZqIbmO00BiAALMOgAC3_T4S340Z0B9V9HRMAQ")
        await callback.message.answer('Проект на тему "UIUX-дизайн"', reply_markup=keyboard2)
        await callback.answer()
        

@router_module_8.callback_query(F.data == 'Методические рекомендации3')
async def method_3(callback: CallbackQuery):
    await update_BD(callback, "Методические рекомендации3")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI93GT_WR_1RDKFtkiF4z4GfilwfRbhAALVOgAC3_T4S7RSt5T2cm0AATAE")
        await callback.message.answer('Проект на тему "Веб-разработка"', reply_markup=keyboard3)
        await callback.answer()
        

@router_module_8.callback_query(F.data == 'Методические рекомендации4')
async def method_4(callback: CallbackQuery):
    await update_BD(callback, "Методические рекомендации4")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI93mT_WZPQaZYxC56EJZhGob03lhJrAALbOgAC3_T4S0GNS1XQ753bMAQ")
        await callback.message.answer('Проект на свободну тему', reply_markup=keyboard4)
        await callback.answer()
        

@router_module_8.callback_query(F.data == 'Шаблон отчёта1')
async def pattern1(callback: CallbackQuery):
    await update_BD(callback, "Шаблон отчёта1")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI97mT_WqjEPKj5qAgI0Jkx2yB1QTLWAALlOgAC3_T4S-9hONV5do_pMAQ")
        await callback.message.answer('Проект на тему "Анализ данных"', reply_markup=keyboard1)
        await callback.answer()


@router_module_8.callback_query(F.data == 'Шаблон отчёта2')
async def pattern2(callback: CallbackQuery):
    await update_BD(callback, "Шаблон отчёта2")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI98GT_WrFzgMKC5bgbnv4bMKka4E1mAALmOgAC3_T4S2p88mY1WDvKMAQ")
        await callback.message.answer('Проект на тему "UIUX-дизайн"', reply_markup=keyboard2)
        await callback.answer()
        

@router_module_8.callback_query(F.data == 'Шаблон отчёта3')
async def pattern3(callback: CallbackQuery):
    await update_BD(callback, "Шаблон отчёта3")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI98mT_WrVSDEOZ4My6-AvUOM6kTp0BAALnOgAC3_T4S5fkAAGjbKyD2DAE")
        await callback.message.answer('Проект на тему "Веб-разработка"', reply_markup=keyboard3)
        await callback.answer()
        

@router_module_8.callback_query(F.data == 'Шаблон отчёта4')
async def pattern4(callback: CallbackQuery):
    await update_BD(callback, "Шаблон отчёта4")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI99GT_WrfW6wg4USZgbtDa25l4PAABwAAC6DoAAt_0-Es5FVqEpWdiLTAE")
        await callback.message.answer('Проект на свободну тему', reply_markup=keyboard4)
        await callback.answer()
        

@router_module_8.callback_query(F.data == 'Доп. материал1')
async def add_material1(callback: CallbackQuery):
    await update_BD(callback, "Доп. материал1")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAI-BGT_XIxaEooUyCQI0DY85UVRZEbOAAL4OgAC3_T4S3FVabFHhZH9MAQ")
        await callback.message.answer('Проект на тему "Анализ данных"', reply_markup=keyboard1)
        await callback.answer()