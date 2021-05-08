from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from constants import PRICES

keyboard = [
        [
            InlineKeyboardButton('Задать вопрос',
                                 callback_data='Задать вопрос'),
            InlineKeyboardButton('Хочу обсудить на приёме',
                                 callback_data='Запись на приём'),
        ],
]

question_keyboard = InlineKeyboardMarkup(keyboard)
