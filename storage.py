import json
import os

class Storage:
  def __init__(self) -> None:
    self.filename = "data.json"
    self.data = {}
    
    if os.path.exists(self.filename):
      with open(self.filename) as f:
        self.data = json.loads(f.read())
  
  def save(self) -> None:
    with open(self.filename, "w") as f:
      f.write(json.dumps(self.data))
  
  def get_all(self) -> list:
    return self.data
  
  def is_exists(self, chat_id, text) -> bool:
    chat_id = str(chat_id)
    if chat_id in self.data:
      return text in self.data[chat_id]
    return False
  
  def add(self, chat_id, text) -> None:
    chat_id = str(chat_id)
    if chat_id in self.data:
      self.data[chat_id].append(text)
    else:
      self.data.update([(chat_id, [text])])
    self.save()