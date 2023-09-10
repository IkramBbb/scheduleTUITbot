from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from keyboards import ikb1, main_m_kb, ikb2, ikb3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlite import db_start, create_profile, is_authorized, select_data
from dotenv import load_dotenv
from service import search_coordinate
import os
from datetime import datetime

load_dotenv()

storage = MemoryStorage()

bot = Bot(os.getenv('TOKEN'))

dp = Dispatcher(bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    name = State()
    course = State()
    faculty = State()
    language = State()


COMMANDS = '''
<b>/start</b> - <em>Запускает Бота</em>
<b>/help</b> - <em>Список команд</em>
<b>/description</b> - <em>Описание бота</em>
<b>/</b> - <em>   </em>'''


async def on_startup(_):
    await db_start()
    print('DONE!!!')


# @dp.message_handler(content_types=['document'])
# async def dl_doc(message: types.Message):
#     await message.document.download(destination_file=message.document.file_name)
#     await message.answer(text=load_exel(filename=message.document.file_name))


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if not await is_authorized(user_id=message.from_user.id):
        await message.answer(text=f"Привет @{message.from_user.username}\n"
                                  f"Я могу подсказат расписание пар\n"
                                  f"Отправьте имя, курс, факултет-направление и язык обучения\n"
                                  f"Посмотеть команды можно тут - /help")
        await ProfileStatesGroup.name.set()
    else:
        await message.answer(f'Привет @{message.from_user.username} рад снова видеть\n'
                             f'Нажми на интересующии кнопку',
                             reply_markup=main_m_kb)


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=COMMANDS, parse_mode='HTML')
    await message.delete()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer(text='На каком курсе учишься?', reply_markup=ikb1)
    await ProfileStatesGroup.next()


# @dp.message_handler(state=ProfileStatesGroup.course)
@dp.callback_query_handler(state=ProfileStatesGroup.course)
async def load_course(message: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['course'] = message.data
    await message.message.edit_text(text='Выбери направление', reply_markup=ikb2)
        # await bot.edit_message_text(chat_id=message.from_user.id,
        #                             text='Выбери направление',
        #                             message_id=(int(message.id) - 2),
        #                             reply_markup=ikb2)
    await ProfileStatesGroup.next()


# @dp.message_handler(state=ProfileStatesGroup.faculty)
@dp.callback_query_handler(state=ProfileStatesGroup.faculty)
async def load_faculty(message: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['faculty'] = message.data
    await message.message.edit_text(text='Выбери язык', reply_markup=ikb3)
    await ProfileStatesGroup.next()


@dp.callback_query_handler(state=ProfileStatesGroup.language)
async def load_lang(message: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['language'] = message.data
    await create_profile(message.from_user.id, state)
    await message.message.delete()
    await message.message.answer(text='Спасибо это всё, теперь я могу подсказать расписание пар', reply_markup=main_m_kb, parse_mode='HTML')
    await state.finish()


@dp.message_handler(Text(equals='Текущая пара'))
async def send_rasp(message: types.Message) -> None:
    # if datetime.now().weekday() == 5:
    #     await message.answer('Сегодня пар нет')
    #     return
    # if datetime.now().weekday() == 6:
    #     await message.answer(f'Сегодня пар нет')
    #     return
    data = await select_data(user_id=message.from_user.id)
    result = search_coordinate(data=data)
    await message.answer(text=result, parse_mode='HTML')


@dp.message_handler(Text(equals='Пары на сегодня'))
async def send_rasp(message: types.Message) -> None:
    if datetime.now().weekday() == 5:
        await message.answer('Сегодня пар нет')
        return
    if datetime.now().weekday() == 6:
        await message.answer(f'Сегодня пар нет')
        return
    await message.answer(f'Сегодня пар нет')
    await message.answer(f'Сегодня пар нет')
    await message.answer(f'Сегодня пар нет')


@dp.message_handler(content_types=['document'])
async def upload_document(message: types.Message):
    if message.from_user.id == os.getenv('ADMIN_ID'):
        await message.document.download(destination_file='Book2.xlsx')
        await message.answer(text='Документ загружен')


@dp.message_handler(commands='go')
async def go(message: types.Message):
    await bot.send_invoice(chat_id=message.chat.id,
                           title='Покупка курса',
                           description='Описание курса',
                           payload='invoice',
                           provider_token='398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065',
                           currency='UZS',
                           prices=[types.LabeledPrice(label='Курс', amount=10000)]
                           )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

