from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from constants import PRICES

keyboard = [
        [InlineKeyboardButton(
            text='Спасибо, я пока тут осмотрюсь...',
            # url='https://card.tochka.com/cjgbrgtye-individualnaia_konsultatsiia',
            callback_data='Не покупаем подписку'
        )],
        [
            InlineKeyboardButton(f'1 месяц ({PRICES[1]} ₽)',
                                 callback_data=PRICES[1]),
            InlineKeyboardButton(f'3 месяца ({PRICES[3]} ₽)',
                                 callback_data=PRICES[3]),
            InlineKeyboardButton(f'Полгода ({PRICES[6]} ₽)',
                                 callback_data=PRICES[6]),
        ],
        [InlineKeyboardButton(f'Год ({PRICES[12]} ₽)',
                              callback_data=PRICES[12])],
]

payment_keyboard = InlineKeyboardMarkup(keyboard)
