from digliboutput import output_book

class search:
  def name(self):
    s_name = input("Enter book name to search")
    o_obj = output_book()
    book_names = o_obj.getdata()
    for book in book_names:
      if s_name == book[0]:
        return True
    else:
      return False