import sqlite3
from diglib import book

class input_book:
  def __init__(self):
    self.db_con = sqlite3.connect('digli.db')
    self.cur_obj = self.db_con.cursor()
    self.cur_obj.execute("CREATE TABLE IF NOT EXISTS books (book_name text, author_name text, publisher text, pages INT, pric INT, weight INT, height INT, width INT, length INT)");

  def inputcli(self):
    name = input("Enter book name: ")
    author = input('Enter author name: ')
    publisher = input('Enter publisher name: ')
    pages = int(input('How many pages are in the book:  '))
    price = int(input('What is the price of the book? '))
    weight = int(input('What is the weight of the book? '))
    height = int(input('What is the height of the book? '))
    width = int(input('What is the width of the book? '))
    length = int(input('What is the length of the book? '))
    #b_n = book(name)
    q = f"INSERT INTO books VALUES ('{name}','{author}','{publisher}','{pages}','{price}','{weight}','{height}','{width}','{length}')"
    self.cur_obj.execute(q)
    self.db_con.commit()
    self.db_con.close()

  def inputfromjson(self):
    pass