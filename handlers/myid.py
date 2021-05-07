def myid(update, context):
    update.message.reply_text(update.message.from_user.id)