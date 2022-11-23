import time
import sqlite3

class Storage:
  def __init__(self) -> None:
    self.filename = "data.db"
    self.connection = sqlite3.connect(self.filename, check_same_thread=False)
    self.cursor = self.connection.cursor()
  
  def find(self, message):
    self.cursor.execute('SELECT value FROM config WHERE key = "time_limit"')
    time_limit = int(self.cursor.fetchone()[0]) * 60 * 60
    now = int(time.time())
    self.cursor.execute("SELECT * FROM messages WHERE chat = ? AND user = ? AND text = ? AND datetime > ?",
                        [message.chat.id, message.from_user.id, message.text, now - time_limit])
    return self.cursor.fetchone()
  
  def add(self, message) -> None:
    self.cursor.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)", [message.chat.id, message.id, message.from_user.id, message.text, message.date])
    self.connection.commit()
    
  def is_admin(self, uuid) -> bool:
    self.cursor.execute('SELECT * FROM config WHERE key = "admin" AND value = ?', [uuid])
    return self.cursor.fetchone() != None
  
  def change_config(self, key, value) -> None:
    self.cursor.execute('UPDATE config SET value = ? WHERE key = ?', [value, key])
    self.connection.commit()
    
  
if __name__ == "__main__":
  s = Storage()
  print(s.is_admin(7301179558))