from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

directions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Frontend', callback_data='frontend'),
            InlineKeyboardButton(text='Backend', callback_data='backend')
        ],
        [
            InlineKeyboardButton(text='AI/ML Engineer', callback_data='ai_ml_engineer'),
            InlineKeyboardButton(text='Data Scientist', callback_data='data_scientist')
        ],
        [
            InlineKeyboardButton(text='Prompt Engineer', callback_data='prompt_engineer'),
            InlineKeyboardButton(text='DevOps / SRE', callback_data='devops_sre')
        ],
        [
            InlineKeyboardButton(text='Cloud Engineer', callback_data='cloud_engineer'),
            InlineKeyboardButton(text='Product Manager', callback_data='product_manager')
        ]
    ]
)
