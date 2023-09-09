from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


ikb1 = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='1', callback_data='1')
ib2 = InlineKeyboardButton(text='2', callback_data='2')
ib3 = InlineKeyboardButton(text='3', callback_data='3')
ib4 = InlineKeyboardButton(text='4', callback_data='4')
ikb1.add(ib1, ib2, ib3, ib4)

main_m_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_m_kb.add('Пары на сегодня').insert('Текущая пара').add('Следуюшая пара').insert('Пары на завтра').add('Настройки')

ikb2 = InlineKeyboardMarkup(row_width=2)
ikb2.add(InlineKeyboardButton(text='KI-AT', callback_data='AT'),
         InlineKeyboardButton(text='KI-KI', callback_data='KI'),
         InlineKeyboardButton(text='KI-DI', callback_data='DI'))

ikb3 = InlineKeyboardMarkup(row_width=2)
ikb3.add(InlineKeyboardButton(text='KK', callback_data='KK'),
         InlineKeyboardButton(text='UZB', callback_data='UZB'),
         InlineKeyboardButton(text='RUS', callback_data='RUS'))
