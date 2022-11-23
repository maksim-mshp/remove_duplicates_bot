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

def change_config(message):
  if storage.is_admin(message.from_user.id):
    try:
      words = message.text.split()
      key = words[0].replace("/set_", "")
      value = int(words[1])
      storage.change_config(key, value)
      bot.reply_to(message, f"✅ {key} успешно изменён")
    except:
      bot.reply_to(message, f"❌ Не удалось изменить {key}")

@bot.message_handler(content_types=['text'])
def all(message):
  words = message.text.split()
  
  if words[0].find("/set_") != -1:
    change_config(message)
    return
  
  r = storage.find(message)
  
  if r != None:
    bot.delete_message(message.chat.id, message.id)
  
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