from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_2 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции2'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ2')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ2'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал2')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами2'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Расписание', url='https://docs.google.com/spreadsheets/d/1PRkm9pfTxrnLbW8UV1fNTpxTXlrdl12kEgdDbsztKKs/edit?gid=0#gid=0')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')]
])

message_text = '2 модуль - Основы алгоритмизации\nhttps://e.vyatsu.ru/course/view.php?id=33138'


@router_module_2.callback_query(F.data == '2 модуль')
async def module_2(callback: CallbackQuery):
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()


@router_module_2.callback_query(F.data == 'Файл с материалами2')
async def file_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAICAWec9pkN_CzZ0oUT3gdJhZbTIioRAAJYawACKx_oSPnYTlf0rAyzNgQ')
        await callback.message.answer(message_text, reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/b2uPoHBWEhE'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/023b78bff739c9fbd6e9e5057e559a2d/?p=bn9MQdqK0BrO-JhwITY6jg'),
     InlineKeyboardButton(text='Материал 1', callback_data='Материал 21')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/h7Z31Okj6tY'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/41b6a0cae818cbd34b0f5215e968d6ed/?p=Tl1pTaRO3glkFF69-4E6QQ'),
     InlineKeyboardButton(text='Материал 2', callback_data='Материал 22')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/j_pq-0v1S1s'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/b12b0342da4561095d344294a280e3f3/?p=4cOD3XigD1xW3St6gNm7ug'),
     InlineKeyboardButton(text='Материал 3', callback_data='Материал 23')],

    [InlineKeyboardButton(text='Видео 4 YT', url='https://youtu.be/2GL8TERJ_zg'),
     InlineKeyboardButton(
        text='Видео 4 RT', url='https://rutube.ru/video/private/34fb3f8f7bc0dcab4fcbf5c87702bb99/?p=KAVs2smdQM2K4chU5nGSsw'),
     InlineKeyboardButton(text='Материал 4', callback_data='Материал 24')],

    [InlineKeyboardButton(text='Видео 5 YT', url='https://youtu.be/yughW7TL8gY'),
     InlineKeyboardButton(
        text='Видео 5 RT', url='https://rutube.ru/video/private/d08cdec4f2798f22a5383572301fc69c/?p=eRKWDk7ygAhUl58cteBuXw&r=plemwd'),
     InlineKeyboardButton(text='Материал 5', callback_data='Материал 25')],

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Лекции2')
async def lect_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лекций 2 модуля', reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_2.callback_query(F.data.startswith('Материал 2'))
async def material_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBpmec607ah0vRtaG2W2M5pOY1xyfcAAKfagACKx_oSFG_oSawwWPxNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBqGec61AcgwABWP9x5laedB89SZMWbAACoGoAAisf6EhFQXP8-RUDbTYE')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBqmec63DsUhRH8hDwt89TM7j9vXd7AAKjagACKx_oSLK_stKLp3oiNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBrGec63IAAXjBxAmTNxMcfXzScOJuiwACpGoAAisf6Ei_LZoUEO0_-DYE')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBrmec65hUHEqNcMciRuhsr9vwYKCRAAKlagACKx_oSKMYWmbW-q6GNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBsGec65x9VaPZRwsHDGGV36juQFfTAAKmagACKx_oSOnDHShQddKzNgQ')
            case 4:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBsmec67-AY6HqE7kAAdMafoGD7OHCHAACqGoAAisf6EgyU4If1W2fjzYE')
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBtGec68LMnDcdAojdzWZYLmk-LxQFAAKpagACKx_oSM2mngpqBj6VNgQ')
            case 5:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBtmec6-a7-TXyPwQZtr199M5A2MxPAAKragACKx_oSPEdGgSDwCdnNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBuGec6-nRilIx0Ibfbr6j22N189gmAAKsagACKx_oSLYREEiY3shkNgQ')

        await callback.message.answer('Раздел лекций 2 модуля', reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/EsuJQtrNIEs'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/76f1d5fcbb0d206a4892e3574618293b/?p=fHRWW0Qg-9eF3HIWcYF5MQ'),
     InlineKeyboardButton(text='Лаб. работа 1', callback_data='Лабораторная работа 21')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/YDov324tQiU'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/143ce393e811e6375c10bc4b117c2c98/?p=9P5hd-leuPtb9Ra4OrDpvA'),
     InlineKeyboardButton(text='Лаб. работа 2', callback_data='Лабораторная работа 22')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/Ab4FtIlAZmQ'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/9a39fd542c111ec52f22e756fcd3c2b2/?p=Jif_el4CS7cxZjlmNOVH7Q&r=plemwd'),
     InlineKeyboardButton(text='Лаб. работа 3', callback_data='Лабораторная работа 23')],

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Материал лаб. работ2')
async def lect_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лабораторных работ 2 модуля', reply_markup=keyboard_labs)
    await callback.answer()


@router_module_2.callback_query(F.data.startswith('Лабораторная работа 2'))
async def lab_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBwGec7NYzfGRA6oaP2CpvY3931V-PAAK6agACKx_oSDDTcKdS0KYfNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBwmec7Ni3jvRE7kDeBlknVy4Jv0CNAAK7agACKx_oSGHGgxX86OCiNgQ')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBvmec7I3RwU2DC-vku5Zm4BHfMoalAAK3agACKx_oSMhioV6FEOnwNgQ')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBumec7GjO-dbhnCrb07hc7k3VIFLOAAKyagACKx_oSNjqv4IZZl50NgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAIBvGec7GuOIJppoATTwe9u3ycfqLwXAAKzagACKx_oSJebtdnMK26vNgQ')
        await callback.message.answer('Раздел лабораторных работ 2 модуля', reply_markup=keyboard_labs)
        await callback.answer()


keyboard_self = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Работа с датами YT', url='https://youtu.be/5Q_-p3nvDEg'),
     InlineKeyboardButton(
         text='Работа с датами RT', url='https://rutube.ru/video/private/31c363acc551fc2b9e530447f069f8c0/?p=_KyLmd0SK6Q8GQAIrh4jdw')],

    [InlineKeyboardButton(text='Работа с JSON YT', url='https://youtu.be/DX1sk2d_R_k'),
     InlineKeyboardButton(
         text='Работа с JSON RT', url='https://rutube.ru/video/private/af0d215a1699077a55e59fdadc9db280/?p=DX7MvVajcHezr4f-_Or6Cw')],

    [InlineKeyboardButton(text='Яндекс контест',
                          callback_data='Яндекс контест 2')],

    [InlineKeyboardButton(text='Диаграмма Ганта',
                          callback_data='Диаграмма Ганта 2')],

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Материалы сам. работ2')
async def self_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел материалов для самостоятельной работы 2 модуля', reply_markup=keyboard_self)
    await callback.answer()


@router_module_2.callback_query(F.data == 'Яндекс контест 2')
async def self_21(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAIBF2ecxuEQSp1j0-cGm_VOSzG6A62jAAKraAACKx_oSB19KYrYK4o-NgQ')
        await callback.message.answer('1 набор задач:\nhttps://official.contest.yandex.ru/contest/41506/\n\n2 набор задач:\nhttps://official.contest.yandex.ru/contest/43747/', disable_web_page_preview=True)
        await callback.message.answer('Раздел материалов для самостоятельной работы 2 модуля', reply_markup=keyboard_self)
        await callback.answer()


@router_module_2.callback_query(F.data == 'Диаграмма Ганта 2')
async def self_22(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAIBxGec7a-_Yqa65c--2gfFChG-8FrQAALEagACKx_oSH7OL5kC2qX1NgQ')
        await callback.message.answer('Раздел материалов для самостоятельной работы 2 модуля', reply_markup=keyboard_self)
        await callback.answer()


keyboard_add = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Основы алгоритмизации и программирования',
                          url='https://moodle.kstu.ru/mod/page/view.php?id=47344')],
    [InlineKeyboardButton(text='Понятие алгоритма. Виды алгоритмов',
                          url='https://intuit.ru/studies/courses/16740/1301/lecture/25624')],
    [InlineKeyboardButton(text='Работа со списками',
                          url='https://devpractice.ru/python-lesson-7-work-with-list/')],
    [InlineKeyboardButton(text='Чем кортеж отличается от списка в Python',
                          url='https://pythonpip.ru/osnovy/chem-kortezh-otlichaetsya-ot-spiska-v-python')],
    [InlineKeyboardButton(text='Множества в Python',
                          url='https://python-scripts.com/sets')],
    [InlineKeyboardButton(text='Очередь в Python',
                          url='https://pythonpip.ru/examples/ochered-python')],
    [InlineKeyboardButton(text='Словари в Python',
                          url='https://pythonru.com/osnovy/python-dict')],
    [InlineKeyboardButton(text='Алгоритмы сортировки на Python',
                          url='https://pythonist.ru/algoritmy-sortirovki-s-python/')],
    [InlineKeyboardButton(text='Функция map',
                          url='https://pythonist.ru/python-map-znakomstvo/')],
    [InlineKeyboardButton(text='Функция filter',
                          url='https://pythonru.com/uroki/funkcija-filter-dlja-nachinajushhih')],
    [InlineKeyboardButton(text='Функция sorted',
                          url='https://pythonru.com/osnovy/vozmozhnosti-i-primery-funkcii-sorted-v-python')],
    [InlineKeyboardButton(text='«O-большое»',
                          url='https://tproger.ru/articles/computational-complexity-explained/')],
    [InlineKeyboardButton(text='Вычислительная сложность алгоритмов', 
                          url='https://www.yuripetrov.ru/edu/python/ch_06_01.html')],
    [InlineKeyboardButton(text='Асимптотические анализ',
                          url='https://codechick.io/tutorials/dsa/dsa')],
    [InlineKeyboardButton(text='Списки и операции над ними',
                          url='https://youtu.be/CEQZYZMPJSU')],
    [InlineKeyboardButton(text='Массивы в Python',
                          url='https://youtu.be/_V4G4A9vehI')],
    [InlineKeyboardButton(text='Вложенные списки',
                          url='https://youtu.be/0qtLrRm36J0')],
    [InlineKeyboardButton(text='Множества в Python',
                          url='https://youtu.be/KMGRXDxUw18')],
    [InlineKeyboardButton(text='Очередь как структура данных',
                          url='https://youtu.be/fmHyFTji-Lc')],
    [InlineKeyboardButton(text='Делаем очередь в Python', 
                          url='https://youtu.be/5i_Gnemfm4o')],
    [InlineKeyboardButton(text='Стек как структура данных', 
                          url='https://youtu.be/B3VHHfMW0Pg')],
    [InlineKeyboardButton(text='Правильная скобочная последовательность',
                          url='https://youtu.be/OTudUhiLNvk')],
    [InlineKeyboardButton(text='Сортировка вставками',
                          url='https://youtu.be/a4IQKxDyR6s')],
    [InlineKeyboardButton(text='Сортировка методом «пузырька»',
                          url='https://youtu.be/5JMInXAtnQg')],
    [InlineKeyboardButton(text='Сортировка слиянием',
                          url='https://youtu.be/XaqR3G_NVoo')],
    [InlineKeyboardButton(text='Быстрая сортировка',
                          url='https://youtu.be/oS5bZdtEhHY')],
    [InlineKeyboardButton(text='Функция map',
                          url='https://www.youtube.com/watch?v=2ghKShXWuSs')],
    [InlineKeyboardButton(text='Функция filter',
                          url='https://www.youtube.com/watch?v=q0xKow-E4Ws')],
    [InlineKeyboardButton(text='Функция sorted',
                          url='https://www.youtube.com/watch?v=Qi5HEyla4_U')],
    [InlineKeyboardButton(text='Вычислительная сложность алгоритма',
                          url='https://youtu.be/rZsZ3LIAUSw')],
    [InlineKeyboardButton(text='Оценка сложности алгоритма. Нотации',
                          url='https://youtu.be/ZRdOb4yR0kk')],
    [InlineKeyboardButton(text='110 функций управления проектами за 12 минут',
                          url='https://www.youtube.com/watch?v=2G1ZiIzI8wo')],

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Доп. материал2')
async def add_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел дополнительных материалов 2 модуля', reply_markup=keyboard_add)
    await callback.answer()
