class Publication:
    def __init__(self, title, author):
      self.title = title
      self.author = author

    def get_title(self) -> str:
      return self.__title

    def get_author(self) -> str:
      return self.__author

    def set_title(self, title: str):
      return self.__title = str(title)

    def set_author(self, author: str):
      return self.__author = str(title)

    def display_info():
      print (f"Title: {title}")
      print (f"Author: {author}")
      
class Book(Publication):
  def __init__(title, author, number_pages):
    self.number_of_pages = number_pages
    
  

if __name__ == "__main__":
    print("Output:")
    print("Account 1")
    accounta1 = BankAccount(676767, 676.67)
    print(f"Account Number: {accounta1.get_account_number()}")
    print(f"Balance: {accounta1.get_balance()}")
    print()
    print(f"Update balance to -150.00")
    accounta1.set_balance(-150.00)
    print(f"Account Number: {accounta1.get_account_number()}")
    print(f"Before Balance: {accounta1.get_balance()}")
    accounta1.set_balance(750.25)
    print(f"After Balance: {accounta1.get_balance()}")
