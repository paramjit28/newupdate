from digliboutput import output_book
from diglib import book
import sqlite3

class delete:


 def delete(self):
    self.db_con = sqlite3.connect('digli.db')
    self.cur_obj = self.db_con.cursor()
    del_book_name = input("What is the book name you want to delete? ")
    q1 = f"DELETE FROM books WHERE book_name Like ('{del_book_name}')"
    self.cur_obj.execute(q1)
    self.db_con.commit()
    print('**** Book has been deleted! ****')
