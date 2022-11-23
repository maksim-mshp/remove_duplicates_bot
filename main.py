import json
import telebot
import json

with open("config.json") as f:
  token = json.loads(f.read())["token"]

bot = telebot.TeleBot(token)


@bot.message_handler()
def echo_all(message):
  bot.delete_message(message.chat.id, message.id)

bot.polling()