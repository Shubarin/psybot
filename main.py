import logging
import os
import threading

from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, \
    CallbackQueryHandler, PreCheckoutQueryHandler

from data import db_session
from handlers import button, help_, myid, start, subscription, \
    precheckout_callback, successful_payment_callback, unsubscribe


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler('help', help_))
    dp.add_handler(CommandHandler('myid', myid))
    dp.add_handler(CommandHandler('subscription', subscription))

    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    dp.add_handler(MessageHandler(Filters.successful_payment,
                                  successful_payment_callback))

    text_handler = MessageHandler(Filters.text, help_)
    dp.add_handler(text_handler)

    main_polling_thread = threading.Thread(target=updater.start_polling)
    unsubsribe_thread = threading.Thread(target=unsubscribe)
    main_polling_thread.start()
    unsubsribe_thread.start()
    main_polling_thread.join()
    unsubsribe_thread.join()
    updater.idle()


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    DB_NAME = os.getenv('DB_NAME')
    LOG_FILENAME = os.getenv('LOG_FILENAME')

    logging.basicConfig(
        level=logging.INFO,
        filename=LOG_FILENAME,
        filemode='a',
        format='%(asctime)s %(levelname)s %(name)s %(message)s'
    )

    db_session.global_init(DB_NAME)
    main()
