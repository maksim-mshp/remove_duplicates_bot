import time
import json
import sqlite3

class Storage:
  def __init__(self) -> None:
    with open("config.json") as f:
      self.filename = json.loads(f.read())["database"]
    self.connection = sqlite3.connect(self.filename, check_same_thread=False)
    self.cursor = self.connection.cursor()
  
  def find(self, message):
    self.cursor.execute('SELECT value FROM config WHERE key = "time_limit"')
    time_limit = int(self.cursor.fetchone()[0]) * 60 * 60
    now = int(time.time())
    self.cursor.execute("SELECT * FROM messages WHERE chat = ? AND user = ? AND text = ? AND datetime > ?",
                        [message.chat.id, message.from_user.id, message.text, now - time_limit])
    return self.cursor.fetchone()
  
  def add(self, chat_id, message_id, user_id, text, words, date) -> None:
    self.cursor.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?, ?)", [chat_id, message_id, user_id, text, words, date])
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