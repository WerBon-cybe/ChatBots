import os
from dotenv import load_dotenv, find_dotenv



TELEGRAM_TOKEN = "5859273218:AAF-SLrEjtWx3ISBPpb3AwN1mg3ypPnqptw"
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = "1851437078"
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = "Привет!👋 С тобой асистент, Макс. Не стесняйся и пиши свой вопрос, а я пока позову операторов тех.поддержки"
REPLY_TO_THIS_MESSAGE = "Не могу переслать сообщение"
WRONG_REPLY = "Пользователь выше не разрешает пересылать его сообщения. Вы должны ответить на ответ бота в разделе переадресованное пользователем сообщение."
