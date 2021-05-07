from data import db_session
from data.users import User
from keyboards import payment_keyboard
from .template_messages import help_text


def start(update, context):
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    full_name = update.message.from_user.full_name
    db_session.get_or_create(User, chat_id=user_id,
                             first_name=first_name,
                             full_name=full_name)
    update.message.reply_text(f'Привет, {first_name}! ' + help_text,
                              reply_markup=payment_keyboard)
