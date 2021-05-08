import logging
import os
import time

import schedule as schedule
from telegram import bot, Bot
from dotenv import load_dotenv

from data import db_session
from data.posts import Posts
from data.users import User
from keyboards import question_keyboard

load_dotenv()
TOKEN = os.getenv('TOKEN')


def send_message(user, db_sess):
    post = db_sess.query(Posts).filter(Posts.id == user.count_posts).first()
    if post:
        user.count_posts += 1
        bot.Bot.send_message(Bot(TOKEN), user.chat_id, post.content,
                             reply_markup=question_keyboard)
    else:
        bot.Bot.send_message(Bot(TOKEN), user.chat_id,
                             'Вы просмотрели все доступные записи 🥳',
                             reply_markup=question_keyboard)


def mailing():
    def job():
        logging.info('Начинаем рассылку')
        db_sess = db_session.create_session()
        users = db_sess.query(User).filter(User.is_active == True)
        for user in users:
            send_message(user, db_sess)
        db_sess.commit()
        logging.info('Сообщения разосланы')

    schedule.every().day.at('14:00').do(job)
    while True:
        schedule.run_pending()
        logging.info('Процесс рассылки засыпает')
        time.sleep(59)
        logging.info('Процесс рассылки просыпается')
