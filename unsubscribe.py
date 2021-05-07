import os
import time
from datetime import datetime

import schedule as schedule
from dotenv import load_dotenv

from data import db_session
from data.users import User


def unsubsribe():
    def job():
        db_sess = db_session.create_session()
        users = db_sess.query(User).filter(
            User.subscription_end==datetime.now().date())
        for user in users:
            user.is_active = False
        db_sess.commit()


    schedule.every().day.at('00:00').do(job)
    while True:
        time.sleep(60 * 60 * 24 - 1)
        schedule.run_pending()

if __name__ == '__main__':
    load_dotenv()
    DB_NAME = os.getenv('DB_NAME')
    db_session.global_init(DB_NAME)
    unsubsribe()