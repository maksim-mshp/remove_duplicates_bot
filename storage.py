import json
import sqlite3

class Storage:
  def __init__(self) -> None:
    self.filename = "data.db"
    self.connection = sqlite3.connect(self.filename, check_same_thread=False)
    self.cursor = self.connection.cursor()
  
  def is_exists(self, message) -> bool:
    self.cursor.execute("SELECT * FROM messages WHERE chat = ? AND user = ? AND text = ?", [message.chat.id, message.from_user.id, message.text])
    return self.cursor.fetchone() != None
  
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