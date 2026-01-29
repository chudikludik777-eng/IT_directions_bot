from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🚀 Что такое IT', callback_data='intro_it'),
            InlineKeyboardButton(text='🧭 Направления', callback_data='it_directions')
        ],
        [
            InlineKeyboardButton(text='🤔 Подойдёт ли мне', callback_data='fit_it')
        ],
        [
            InlineKeyboardButton(text='📚 С чего начать', callback_data='start_learning')
        ],
        [
            InlineKeyboardButton(text='🎯 Выбрать путь', callback_data='choose_path')
        ],
        [
            InlineKeyboardButton(text='💡 Случайный совет', callback_data='random_tip')
        ]
    ]
)
