import logging
import time
from datetime import datetime, timedelta

import schedule as schedule

from data import db_session
from data.users import User


def unsubscribe():
    def job():
        logging.info('Отписываем пользователей')
        db_sess = db_session.create_session()
        yesterday = datetime.now().date() - timedelta(days=1)
        users = db_sess.query(User).filter(
            User.subscription_end <= yesterday, User.is_active == True)
        for user in users:
            user.is_active = False
        db_sess.commit()
        logging.info('Unsubscribe success fo users: '
                     f'{", ".join(map(str, users))}')

    schedule.every().day.do(job)
    while True:
        schedule.run_pending()
        logging.info('Процесс отписки засыпает')
        time.sleep(60 * 60 * 24 - 1)
        logging.info('Процесс отписки просыпается')
