import json
import telebot
from storage import Storage

with open("config.json") as f:
  token = json.loads(f.read())["token"]

bot = telebot.TeleBot(token)
s = Storage()


@bot.message_handler()
def echo_all(message):
  if s.is_exists(message.chat.id, message.text):
    bot.delete_message(message.chat.id, message.id)
  else:
    s.add(message.chat.id, message.text)

bot.polling()