from datetime import datetime
import os

class Logger:
  def prepare_file(self, error) -> str:
    filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S.%f") + ".log"
    with open(filename, "w+") as f:
      f.write(error)
    return filename
  
  def remove_file(self, filename) -> None:
    if os.path.exists(filename):
      os.remove(filename)
      
  def log(self, bot, error) -> None:
    with open("errors.log", "a+") as f:
      f.write(error)
      f.write("\n")
      
    filename = self.prepare_file(error)      
    bot.send_document(730117958, open(filename, "rb"))
    self.remove_file(filename)