from diglibinput import input_book
from diglibsearch import search
from digliboutput import output_book
from diglibdelete import delete
import sys

def menu():
  print()
  choice = int(input("""
                      1: Enter new book record
                      2: Search if book exist
                      3: Get all books in library
                      4: Delete - delete
                      5: Exit
                      Please enter your choice: """))

  if choice == 1:
    inpobj = input_book()
    inpobj.inputcli()
  elif choice == 2:
    s_obj = search()
    print(s_obj.name())
  elif choice == 3:
    o_obj = output_book()
    print(o_obj.getdata())
  elif choice == 4:
    del_obj = delete()
    del_obj.delete()
  elif choice == 5:
    sys.exit()
  else:
    print("Invalide choice, You must select between 1 and 5")
    print("Please try again")
    menu()

if __name__ == "__main__":
  while True:
    menu()
