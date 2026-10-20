#creating class publication
class Publication:
    def __init__(self, title, author): #title and author are being initialized
      self.title = title
      self.author = author

    def get_title(self) -> str: #getting title expected to be string
      return self.title

    def get_author(self) -> str:
      return self.author

    def set_title(self, title: str):
      return self.title = str(title)

    def set_author(self, author: str):
      return self.author = str(title)

    def display_info():
      print (f"Title: {title}")
      print (f"Author: {author}")
      
class Book(Publication):
    def __init__(title, author, number_pages):
        self.number_of_pages = number_pages

    def get_number_of_pages():
        return number_pages

    def set_number_of_pages:
        return self.number_pages = int(number_pages)

class Magazine(Publication):
    def __init__(title, author, issue_number):
        self.issue_number = issue_number

    def get_issue_number():
        return self.issue_number

    def set_issue_number(issue_number): 
        return self.issue_number = int(issue_number)
  

if __name__ == "__main__":
    #Objects being created :)
    pub = Publication("Charles Scribner's Sons", "Ratchiff, R. & Van Dongen, H.")
    book = Book("The Great Gatsby",  "F. Scott Fitzgerald", 218)
    mag = Magazine("National Geographic", "Various Authors", 202)

    #this is how you print the info yes
    print("Publication Information:")
    pub.display_info
    print()
    print("Information for book:")
    book.set_number_of_pages(-310)
    book.display_info()
    print(book.get_number_of_pages())
    print()
    print("Information for Magazine:")
    mag.display_info()
    print(mag.get_issue_number())
