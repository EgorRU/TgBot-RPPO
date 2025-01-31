from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_1 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции1'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ1')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ1'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал1')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами1'),
     InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=760514')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '1 модуль - Основы программирования на Python\nhttps://e.vyatsu.ru/course/view.php?id=33137'


@router_module_1.callback_query(F.data == '1 модуль')
async def module_1(callback: CallbackQuery):
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Файл с материалами1')
async def file_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAMwZ5y3kd7uvj1p-sVaPpw51c2ZYewAAmxcAAI9-ulI-IR13-5bJMQ2BA')
        await callback.message.answer(message_text, reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/FK-sqG2mrlk'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/a71285c49bc9913a235a3c974d273a16/?p=mAOJtzxMgChUazhqE5FTOw'),
     InlineKeyboardButton(text='Материал 1', callback_data='Материал 11')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/1fJ3LFlWY3I'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/9f391693367112dcfdf66423af93e9b9/?p=nXqZP866epnlj-rJ3PAF_w'),
     InlineKeyboardButton(text='Материал 2', callback_data='Материал 12')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/eJRZwVaix9s'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/07c529d2ce4abc89fa15f46c5ea42151/?p=Z9ezRt5jMuwnclEugpcQMQ'),
     InlineKeyboardButton(text='Материал 3', callback_data='Материал 13')],

    [InlineKeyboardButton(text='Видео 4 YT', url='https://youtu.be/GP0jUYaZBHs'),
     InlineKeyboardButton(
        text='Видео 4 RT', url='https://rutube.ru/video/private/75e160d6b51d17101cc4a89d8a31771b/?p=ny_BHjkBITyUx_eR00n9SA'),
     InlineKeyboardButton(text='Материал 4', callback_data='Материал 14')],

    [InlineKeyboardButton(text='Видео 5 YT', url='https://youtu.be/cQ7_4Lg99sw'),
     InlineKeyboardButton(
        text='Видео 5 RT', url='https://rutube.ru/video/private/43beaf9edd9e7aa1f2ac66d3fcb9eb4e/?p=wcHVzqd6dSfubJhAkiJGgw'),
     InlineKeyboardButton(text='Материал 5', callback_data='Материал 15')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Лекции1')
async def lect_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лекций 1 модуля', reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_1.callback_query(F.data.startswith('Материал 1'))
async def material_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAANBZ5y80WBjoV5ecPIt6ooBGExt_bwAAqBcAAI9-ulIKjRz_Yeyqt02BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAANDZ5y81iWdhNVB_urDGtYdlTEIzBEAAqFcAAI9-ulIdQ4sYYlA2EQ2BA')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAANFZ5y9x4B2qbMCqKpx9ZrSKID1vVQAAqxcAAI9-ulIbtY1_ZJ5Mfc2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAANHZ5y9z9ecaCg4NAAB8FZD3lU701ngAAKtXAACPfrpSBZ2l6SbroNkNgQ')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOOZ5zAfc-DKYupX8NWdJQ89p3E9iUAAutcAAI9-ulI5bdHEmcxejY2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOQZ5zAg-qzdbaGswSY7miVoANfGOIAAuxcAAI9-ulIdLBxvu9SeHI2BA')
            case 4:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOfZ5zA2i1CoGPmAQE9brSALYJ3tfIAAu5cAAI9-ulIk_h9r-LZ3Zg2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOhZ5zA3pL6kql0aVC5Wln7br-pFY8AAu9cAAI9-ulIroOF9avrqVk2BA')
            case 5:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOjZ5zA_le8SQcKcZcNbG8kOSxExoMAAvJcAAI9-ulIK8MAAfSoy4H5NgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOlZ5zBATaOLo-OF96V0lCXKKnjfV8AAvNcAAI9-ulICeeig2qYb6E2BA')

        await callback.message.answer('Раздел лекций 1 модуля', reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/hSL4B9DM0k0'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/52ba5e84ee5dac25f6f33ca0256ba12b/?p=CEZUgcXbvFdiI_JxK3TMYg'),
     InlineKeyboardButton(text='Лаб. работа 1', callback_data='Лабораторная работа 11')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/VLG_XnVteiM'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/8db4704c2e990d8a718d4d117b914203/?p=Q0D8tD1W91TMQiLfIBThpA'),
     InlineKeyboardButton(text='Лаб. работа 2', callback_data='Лабораторная работа 12')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/Iqrm9fL6N00'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/6a2173e9e5889e6e746478459f0fe95b/?p=OiZe9b1CMtK5QuKmlBhhdA'),
     InlineKeyboardButton(text='Лаб. работа 3', callback_data='Лабораторная работа 13')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Материал лаб. работ1')
async def lect_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лабораторных работ 1 модуля', reply_markup=keyboard_labs)
    await callback.answer()


@router_module_1.callback_query(F.data.startswith('Лабораторная работа 1'))
async def lab_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAPYZ5zDabD8xTwzc34_EAABy-ykxX1rAAIIXQACPfrpSMYDcqX2p-zZNgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAPXZ5zDaddeZBQVe17oO5ACLIZE3HMAAgldAAI9-ulIqJGzN7Z_8aQ2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAPWZ5zDaWfTgfPvd-c0ZlZ97kwWU1YAAgddAAI9-ulIoSzzDdB00Y42BA')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAPeZ5zDmBhevPX9TCakd_OwjAe9ju8AAg5dAAI9-ulItna5luVCdtk2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAPdZ5zDmNO7uejn7G-uKWKiAkCu5OcAAg1dAAI9-ulIVaN9x9bAssM2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAPcZ5zDmFqcwYU1qiAZFjOwTi9PUbkAAgxdAAI9-ulIOuZ8wzMjRtI2BA')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAPkZ5zDyhUiFA9xQTQMmsTo-zslVHMAAhVdAAI9-ulI0xp2Yr3hJyk2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAPjZ5zDykLy0N_n0H8SFtYICJCHwNUAAhRdAAI9-ulIaK7b91HjYkw2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAPiZ5zDypJHnLo2UiJj1lXcfGPyKdoAAhNdAAI9-ulIi6OMaJ9xHVU2BA')
        await callback.message.answer('Раздел лабораторных работ 1 модуля', reply_markup=keyboard_labs)
        await callback.answer()


keyboard_self = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Элементарная графика YT', url='https://youtu.be/ibWo576pW5M'),
     InlineKeyboardButton(
         text='Элементарная графика RT', url='https://rutube.ru/video/private/53dfb64235f3f13dd6b5dc30f77bab92/?p=-4zjc5W0fgh4-Q9RUSomEw')],

    [InlineKeyboardButton(text='Работа с файлами YT', url='https://youtu.be/GDqFig4IM7U'),
     InlineKeyboardButton(
         text='Работа с файлами RT', url='https://rutube.ru/video/private/414c12b74c6878034caaf8020722ff67/?p=4f4s0Ux5hX95TxTORrE4Cg')],

    [InlineKeyboardButton(text='Яндекс контест',
                          callback_data='Яндекс контест 1')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Материалы сам. работ1')
async def self_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел материалов для самостоятельной работы 1 модуля', reply_markup=keyboard_self)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Яндекс контест 1')
async def self_11(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAIBF2ecxuEQSp1j0-cGm_VOSzG6A62jAAKraAACKx_oSB19KYrYK4o-NgQ')
        await callback.message.answer('1 набор задач:\nhttps://official.contest.yandex.ru/contest/41063/\n\n2 набор задач:\nhttps://official.contest.yandex.ru/contest/41305/', disable_web_page_preview=True)
        await callback.message.answer('Раздел материалов для самостоятельной работы 1 модуля', reply_markup=keyboard_self)
        await callback.answer()


keyboard_add = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Установка и настройка IDE PyCharm Community Edition',
                          url='http://inf-w.ru/wp-content/uploads/2018/08/Методичка-PyCharm.pdf')],
    [InlineKeyboardButton(text='Каким должен быть код на Python',
                          url='https://all-python.ru/osnovy/pep-8.html')],
    [InlineKeyboardButton(text='Лучшие примеры форматирования строк в Python',
                          url='https://python-scripts.com/string-formatting')],
    [InlineKeyboardButton(text='Работа с файлами 1',
                          url='https://all-python.ru/osnovy/rabota-s-fajlami.html')],
    [InlineKeyboardButton(text='Работа с файлами 2',
                          url='https://ppt-online.org/259112')],
    [InlineKeyboardButton(text='Работа с текстовыми файлами',
                          url='https://all-python.ru/osnovy/tekstovye-fajly.html')],
    [InlineKeyboardButton(text='Графика в Python при помощи модуля turtle',
                          url='https://geekstand.top/development/grafika-v-python-pri-pomoshhi-modulja-turtle/')],
    [InlineKeyboardButton(text='Побитовые операторы (bitwise) в Python',
                          url='https://pythonim.ru/osnovy/pobitovye-operatory-bitwise-v-python')],
    [InlineKeyboardButton(text='30 основных встроенных функций python',
                          url='https://pythonru.com/osnovy/vstroennye-funkcii-python')],
    [InlineKeyboardButton(text='Самоучитель проекта pythonworld',
                          url='https://pythonworld.ru/pdf')],
    [InlineKeyboardButton(text='Инди-курс программирования на Python',
                          url='https://stepik.org/course/63085/promo')],

    [InlineKeyboardButton(text='Как создать функцию, как с ними работать',
                          url='https://rutube.ru/video/4b00ef8ea1729ba3c4dcb46c1785c070/')],
    [InlineKeyboardButton(
        text='Try-except', url='https://www.youtube.com/watch?v=ZQGU3CKMlW0')],
    [InlineKeyboardButton(text='Встроенные функции Python',
                          url='https://www.youtube.com/watch?v=j8Dm8ORobTc')],
    [InlineKeyboardButton(text='Функция map',
                          url='https://youtu.be/_RA35zG-0gA')],
    [InlineKeyboardButton(text='Побитовые операторы',
                          url='https://www.youtube.com/watch?v=nwBKiIx3gsE')],
    [InlineKeyboardButton(text='Знакомство с модулем Turtle',
                          url='https://www.youtube.com/watch?v=WIWHPDN7CTI')],
    [InlineKeyboardButton(text='Рисуем с помощью черепашки: модуль turtle',
                          url='https://www.youtube.com/watch?v=l4BN3e70nFU')],
    [InlineKeyboardButton(text='Python Turtle Graphics Games',
                          url='https://www.youtube.com/watch?v=uPxIgqRKRtY')],
    [InlineKeyboardButton(
        text='Работа с файлами: чтение из файла 1', url='https://youtu.be/fJKkBUOq2Z4')],
    [InlineKeyboardButton(
        text='Работа с файлами: чтение из файла 2', url='https://youtu.be/AJZ1xq9_caE')],
    [InlineKeyboardButton(text='Запись данных в файл в текстовом и бинарном режимах',
                          url='https://www.youtube.com/watch?v=vJ0PZQj9AUs')],
    [InlineKeyboardButton(text='Работа с файлами в Python. Чтение и запись данных',
                          url='https://www.youtube.com/watch?v=oRr_bEXJbV0')],
    [InlineKeyboardButton(text='Работа со строками 1',
                          url='https://youtu.be/YUMJxjsfNt4')],
    [InlineKeyboardButton(text='Работа со строками 2',
                          url='https://youtu.be/ITI2kJ6j8Ho')],
    [InlineKeyboardButton(text='Работа со строками 3',
                          url='https://youtu.be/GmMD6gQYWe4')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Доп. материал1')
async def add_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел дополнительных материалов 1 модуля', reply_markup=keyboard_add)
    await callback.answer()
