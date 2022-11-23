import json
import os

class Storage:
  def __init__(self) -> None:
    self.filename = "data.json"
    self.data = []
    
    if os.path.exists(self.filename):
      with open(self.filename) as f:
        self.data = json.loads(f.read())
  
  def get_all(self) -> list:
    return self.data
  
if __name__ == "__main__":
  s = Storage()
  print(s.get_all())