import os
from telegram.ext import Updater, MessageHandler, Filters
from telegram import ChatMember

def delete_links(update, context):
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    member = chat.get_member(user.id)

    if member.status not in [ChatMember.ADMINISTRATOR, ChatMember.CREATOR]:
        if 'http' in message.text or 't.me/' in message.text:
            try:
                message.delete()
                print(f"Deleted link from {user.username}")
            except Exception as e:
                print(f"Error deleting message: {e}")

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), delete_links))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
