import datetime
import calendar

from constants import PRICES
from data import db_session
from data.users import User


def precheckout_callback(update, context) -> None:
    query = update.pre_checkout_query
    if query.invoice_payload != 'Custom-Payload':
        query.answer(ok=False, error_message="Something went wrong...")
    else:
        user_id = query.from_user.id
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.chat_id == user_id).first()
        price = query.total_amount // 100
        if not user.is_active:
            subscription_end = get_subscription_end(price)
            user.is_active = True
            user.subscription_start = datetime.datetime.now()
        else:
            subscription_end = get_subscription_end(price,
                                                    user.subscription_end)
        user.subscription_end = subscription_end
        db_sess.commit()
        query.answer(ok=True)


def successful_payment_callback(update, context) -> None:
    update.message.reply_text('Мы получили оплату. Спасибо!')


def get_subscription_end(price, start_date=None):
    n = 0
    for months, val in PRICES.items():
        if price == val:
            n = months
    if not start_date:
        start_date = datetime.datetime.now().date()
    cur_date = start_date
    for i in range(n):
        increment_days_count = calendar.mdays[cur_date.month]
        cur_date += datetime.timedelta(days=increment_days_count)
    return cur_date
