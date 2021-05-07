from keyboards import payment_keyboard
from .template_messages import help_text


def help_(update, context):
    update.message.reply_text('/myid - узнать свой чат-id')
    update.message.reply_text('/subscription - узнать информацию '
                              'о своей подписке')
    update.message.reply_text(help_text,
                              reply_markup=payment_keyboard)
