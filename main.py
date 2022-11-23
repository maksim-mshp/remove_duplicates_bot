from decimal import DivisionByZero
import json
import telebot
import traceback
import sys
from storage import Storage
from logger import Logger

with open("config.json") as f:
  token = json.loads(f.read())["token"]

bot = telebot.TeleBot(token)
storage = Storage()
logger = Logger()

@bot.message_handler()
def echo_all(message):
  if storage.is_exists(message.chat.id, message.text):
    bot.delete_message(message.chat.id, message.id)
  else:
    storage.add(message.chat.id, message.text)
    
def start():
  while True:
    try:
      bot.polling(none_stop=True)
    except:
      exc_type, exc_value, exc_traceback = sys.exc_info()
      lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
      error = "".join(line for line in lines)
      
      logger.log(bot, error)
      
if __name__ == "__main__":
  start()