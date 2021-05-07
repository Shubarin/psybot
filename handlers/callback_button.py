import logging
import os

from dotenv import load_dotenv
from telegram import Update, LabeledPrice

load_dotenv()


def start_without_shipping_callback(update, context, price) -> None:
    chat_id = update.callback_query.from_user.id
    logging.info(f'chat_id: {chat_id} начал оформлять подписку')
    title = 'Оформление подписки'
    description = 'Подписка на онлайн-консультацию'
    payload = 'Custom-Payload'
    provider_token = os.getenv('PAYMENTS_PROVIDER_TOKEN')
    currency = 'RUB'
    prices = [LabeledPrice('Подписка', price * 100)]

    context.bot.send_invoice(
        chat_id, title, description, payload, provider_token, start_parameter=None, currency=currency, prices=prices
    )


def button(update: Update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'Не покупаем подписку':
        query.edit_message_text(text='Очень жаль, полный функционал '
                                     'доступен только в платной версии')
    else:
        price = int(query.data)
        start_without_shipping_callback(update, context, price)
        # query.edit_message_text(text=query.data)
