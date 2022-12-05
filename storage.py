import time
import json
import sqlite3
from functions import is_duplicate

class Storage:
  def __init__(self) -> None:
    with open("config.json") as f:
      self.filename = json.loads(f.read())["database"]
    self.connection = sqlite3.connect(self.filename, check_same_thread=False)
    self.cursor = self.connection.cursor()
  
  def check(self, chat_id, message_id, words):
    length = int(self.get_config('length'))
    
    if len(words) <= length:
      return True
    
    time_limit = int(self.get_config('time_limit')) * 60 * 60
    now = int(time.time())
    max_intersection = int(self.get_config('intersection'))
    posts_limit = int(self.get_config('posts_limit'))
    
    self.cursor.execute("SELECT * FROM messages WHERE chat = ? AND user = ? AND datetime > ? AND length > ?",
                        [chat_id, message_id, now - time_limit, length])
    
    messages = set()
    
    for i in self.cursor.fetchall():
      i_words = i[3].split()
      minimum = min(len(words), len(i_words))
      maximum = max(len(words), len(i_words))
      
      messages.add(i[3])
      
      if (minimum / maximum) <= (max_intersection / 100):
        continue
      elif is_duplicate(words, i_words, max_intersection):
          return False
          
    return len(messages) < posts_limit
  
  def add(self, chat_id, message_id, user_id, text, length, date) -> None:
    self.cursor.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?, ?)", [chat_id, message_id, user_id, text, length, date])
    self.connection.commit()
    
  def is_admin(self, uuid) -> bool:
    with open("config.json") as f:
      admins = json.loads(f.read())["admins"]
      return uuid in admins
  
  def change_config(self, key, value) -> None:
    self.cursor.execute('UPDATE config SET value = ? WHERE key = ?', [value, key])
    self.connection.commit()
    
  def get_config(self, key) -> str:
    self.cursor.execute("SELECT value from config WHERE key = ?", [key])
    return self.cursor.fetchone()[0]
    
  
if __name__ == "__main__":
  s = Storage()
  print(s.get_config('time_limit'))