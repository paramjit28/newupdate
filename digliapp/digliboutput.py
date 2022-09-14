import sqlite3

class output_book:
  def __init__(self):
    self.db_con = sqlite3.connect('digli.db')
    self.cur_obj = self.db_con.cursor()

  def getdata(self):
    self.cur_obj.execute("select * from books")
    return self.cur_obj.fetchall()
