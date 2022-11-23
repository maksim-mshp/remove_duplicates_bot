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

@bot.message_handler(commands=["/set_time_limit"])
def set_time_limit(message):
  if storage.is_admin(message.from_user.id):
    try:
      time_limit = int(message.text.split()[1])
      storage.set_time_limit(time_limit)
    except:
      bot.reply_to(message, "❌ Не удалось изменить time_limit")

@bot.message_handler()
def echo_all(message):
  if storage.is_exists(message):
    bot.delete_message(message.chat.id, message.id)
  else:
    storage.add(message)
    
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