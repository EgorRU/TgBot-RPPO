from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_3 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции3'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ3')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ3'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал3')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами3'),
     InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/course/view.php?id=33139&sectionid=2681099')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')]
])

message_text = '3 модуль - Базы данных и реляционная алгебра\nhttps://e.vyatsu.ru/course/view.php?id=33139'


@router_module_3.callback_query(F.data == '3 модуль')
async def module_3(callback: CallbackQuery):
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()


@router_module_3.callback_query(F.data == 'Файл с материалами3')
async def file_3(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAICAWec9pkN_CzZ0oUT3gdJhZbTIioRAAJYawACKx_oSPnYTlf0rAyzNgQ')
        await callback.message.answer(message_text, reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/DqaFNejpA1c'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/90770f3af10fc82668e997e28c76244b/?p=mPc3ev02EUMuBJLm213DCg'),
     InlineKeyboardButton(text='Материал 1', callback_data='Материал 31')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/ViBLgHyxsHI'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/2ba9aadb203fc088562063f7ce492b2e/?p=1IfbN-lsrZHLImIL0OGoWg'),
     InlineKeyboardButton(text='Материал 2', callback_data='Материал 32')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/-WNZte7Rgn4'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/1e944fdd2c1902a6814d8ea5a96ce90a/?p=sUL_SRiLmXjbDe0Mq8Mwww'),
     InlineKeyboardButton(text='Материал 3', callback_data='Материал 33')],

    [InlineKeyboardButton(text='Видео 4 YT', url='https://youtu.be/bdt9ffXfn3c'),
     InlineKeyboardButton(
        text='Видео 4 RT', url='https://rutube.ru/video/private/922bef753979a58bfdaeb9e24efda304/?p=UcTnPwfL3ePC3fw8enNgzA'),
     InlineKeyboardButton(text='Материал 4', callback_data='Материал 34')],

    [InlineKeyboardButton(text='Видео 5 YT', url='https://youtu.be/bdt9ffXfn3c'),
     InlineKeyboardButton(
        text='Видео 5 RT', url='https://rutube.ru/video/private/e87943c93629002474e0b98f8b8a4e15/?p=VaBZJrBAfFcM0MQZ7l6kgQ'),
     InlineKeyboardButton(text='Материал 5', callback_data='Материал 35')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Лекции3')
async def lect_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лекций 3 модуля', reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_3.callback_query(F.data.startswith('Материал 3'))
async def material_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICo2e60Evz_fUAAQcAAd46KpbZbVtp2mcAAuJeAAL1QNhJwa0AAbLQPkOENgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICpWe60E7NjmgmRcCo3Y_fWrRYWgcGAALjXgAC9UDYSRsHapREAo7DNgQ')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICp2e60IC80WuE8zbx_trTTS7PD8LvAALmXgAC9UDYSTpYjjeZG9SLNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICqWe60IV6Uv0BncgNNGw4uW6vHkk2AALnXgAC9UDYSewj-fG_55u8NgQ')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICq2e60KMsYBz8avGnXBOpSs2j6bxbAALpXgAC9UDYSedhH9MHzkqoNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICrWe60KhwuNUMJJqtNLajy1wISbnPAALqXgAC9UDYSbIFCGQEZ6uDNgQ')
            case 4:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICr2e60MxdKWYrySo598-U2x330yEiAALrXgAC9UDYSW7g-ezK4_PMNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICsWe60NFlWLyF6CRiL5POjB5MYM7_AAIcXAAC6wAB2UmUC03-B7wMrzYE')
            case 5:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICs2e60PP-rTBBjhzZoupX_3vL6yiHAALsXgAC9UDYSbn5aVYJvrwaNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICtWe60PjjQGunkoDjul0upaG1v3bGAALuXgAC9UDYSfQ0hiIdAhvCNgQ')

        await callback.message.answer('Раздел лекций 3 модуля', reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/4vdLfuCDdaA'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/7c9e4f809ee27fe761cb23f4d3a401d5/?p=cXTgiPF96F-bmZabPJA0-A'),
     InlineKeyboardButton(text='Лаб. работа 1', callback_data='Лабораторная работа 31')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/JGaIxyl6USY'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/f3b8bbf900d2bcdf8e3f23491488b085/?p=FjPb-aDblzu6Y_TDyDohow'),
     InlineKeyboardButton(text='Лаб. работа 2', callback_data='Лабораторная работа 32')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/w6JohrkV3rs'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/c64165123218b965cc74f3ebaf5282ee/?p=55Jc2l1HgQ6dT21yRiHmHw'),
     InlineKeyboardButton(text='Лаб. работа 3', callback_data='Лабораторная работа 33')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Материал лаб. работ3')
async def lect_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лабораторных работ 3 модуля', reply_markup=keyboard_labs)
    await callback.answer()


@router_module_3.callback_query(F.data.startswith('Лабораторная работа 3'))
async def lab_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICt2e60SdE2HbELYyDwE1ELVwiASkbAAIgXAAC6wAB2UlwfMnh4dPrUzYE')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICuWe60SqGcMpqweF6fx74T7a_m7sUAAIhXAAC6wAB2UmJmG5WvbRoXTYE')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICu2e60TI2ogLptQ5efVp_ahjZsgABgwACIlwAAusAAdlJcmvFdgEBtfM2BA')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICvWe60XWmPbPBY6M4bOGilRSxuU5eAAL2XgAC9UDYSfZfrIbSm1HONgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICv2e60XguJ2_ecX5lZ-qq4bw4_VBkAAL3XgAC9UDYSVr7lnxjsr05NgQ')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAICwWe60bTbd4X4SBay1rJnwYXUw23AAAL7XgAC9UDYSeqfT45SsOfDNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICw2e60bjspC17GjGXAfThCQ2-FeoaAAL8XgAC9UDYSSwWETpC9AcpNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICxWe60buCB737jpVOn0uaiN3_FD-KAAL9XgAC9UDYSbXfHZoe9509NgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICx2e60b_EF8vxySSIRMz1MlJ3polOAAL-XgAC9UDYSZKanzdSBeRBNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAICyWe60cIn9jvbpjKoZqXFL8LF92ChAAL_XgAC9UDYSYeRSsEDPfypNgQ')
        await callback.message.answer('Раздел лабораторных работ 3 модуля', reply_markup=keyboard_labs)
        await callback.answer()


keyboard_self = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='pgAdmin YT', url='https://youtu.be/pJ9D_jpEw-w'),
     InlineKeyboardButton(
         text='pgAdmin RT', url='https://rutube.ru/video/private/59dcf90b888f649bea64ca4079f6f517/?p=k43Bp9HRzC1Coh4Q4n0p1A')],

    [InlineKeyboardButton(text='Проектирование бд YT', url='https://youtu.be/MoCX1IK-VMg'),
     InlineKeyboardButton(
         text='Проектирование бд RT', url='https://rutube.ru/video/private/3d103ae4d9b0e59f1e4eb8c636be4221/?p=HdMTQrtsWMCziBYiAN0hpg')],

    [InlineKeyboardButton(text='Построение ER-диаграмм',
                          callback_data='Построение ER-диаграмм3')],

    [InlineKeyboardButton(text='Проектирование средствами pgAdmin',
                          callback_data='Проектирование средствами pgAdmin3')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Материалы сам. работ3')
async def self_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел материалов для самостоятельной работы 3 модуля', reply_markup=keyboard_self)
    await callback.answer()


@router_module_3.callback_query(F.data == 'Построение ER-диаграмм3')
async def self_31(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAICy2e60tjoHREnOOSPMd_UIaVrPDkqAAIUXwAC9UDYSUhpVkdZHuXSNgQ')
        await callback.message.answer_document(document='BQACAgIAAxkBAAICzWe60tzVQMOBFkCmdsnnsG1qukMsAAIVXwAC9UDYSU4IkbJFK0U4NgQ')
        await callback.message.answer('Раздел материалов для самостоятельной работы 3 модуля', reply_markup=keyboard_self)
        await callback.answer()


@router_module_3.callback_query(F.data == 'Проектирование средствами pgAdmin3')
async def self_32(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAICz2e60wqJQXQwhKHrRE2xbY4XsTrBAAIdXwAC9UDYSfDBk5K4XLL_NgQ')
        await callback.message.answer('Раздел материалов для самостоятельной работы 3 модуля', reply_markup=keyboard_self)
        await callback.answer()


keyboard_add = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создание таблиц в pgAdmin',
                          url='https://youtu.be/jM5yAeHmgm8')],
    [InlineKeyboardButton(text='Создание столбцов в pgAdmin',
                          url='https://youtu.be/5yWvUjWwJFU')],
    [InlineKeyboardButton(text='Первичный ключ',
                          url='https://youtu.be/pRa43sJmAv8')],
    [InlineKeyboardButton(text='Создание столбца для хранения даты',
                          url='https://youtu.be/RnDifFgyH1w')],
    [InlineKeyboardButton(text='Создание внешних ключей',
                          url='https://youtu.be/y0qz_AV3aIM')],
    [InlineKeyboardButton(text='Схема взаимодействия',
                          url='https://youtu.be/xGiZr-aAdHM')],
    [InlineKeyboardButton(text='Добавление тестовых данных',
                          url='https://youtu.be/9oaUnZHfwd4')],
    [InlineKeyboardButton(text='Первая нормальная форма',
                          url='https://youtu.be/MprdbcJzAXI')],
    [InlineKeyboardButton(text='Вторая нормальная форма',
                          url='https://youtu.be/hmr-A1dg4U4')],
    [InlineKeyboardButton(text='Третья нормальная форма',
                          url='https://youtu.be/8HRaJAgostc')],
    [InlineKeyboardButton(text='Онлайн-курс «Базы данных» 1',
                          url='https://stepik.org/course/2614/promo?search=1216613643')],
    [InlineKeyboardButton(text='Онлайн-курс «Базы данных» 2', 
                          url='https://openedu.ru/program/spbu/BDWORK/')],
    [InlineKeyboardButton(text='Что такое База Данных',
                          url='https://habr.com/ru/articles/555760/')],
    [InlineKeyboardButton(text='Путеводитель по базам данных',
                          url='https://habr.com/ru/companies/otus/articles/561100/')],
    [InlineKeyboardButton(text='Базы данных: большой обзор',
                          url='https://habr.com/ru/companies/yandex/articles/522164/')],
    [InlineKeyboardButton(text='Основы современных баз данных',
                          url='https://citforum.ru/database/osbd/contents')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Доп. материал3')
async def add_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел дополнительных материалов 3 модуля', reply_markup=keyboard_add)
    await callback.answer()
