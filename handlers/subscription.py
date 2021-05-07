from data import db_session
from data.users import User
from keyboards.payments import payment_keyboard


def subscription(update, context):
    user_id = update.message.from_user.id
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.chat_id == user_id,
                                      User.is_active == True).first()
    if not user:
        update.message.reply_text('У тебя нет действующей подписки. А зря, '
                                  'она дает много преимуществ 😉',
                                  reply_markup=payment_keyboard)
    else:
        update.message.reply_text(f'У тебя оформлена подписка. '
                                  'Начало действия подписки '
                                  f'{user.subscription_start}. '
                                  'Подписка закончится '
                                  f'{user.subscription_end}')
