#Created class publication
class Publication:
    def __init__(self, title, author): #self, title, and author are initializeed
        self.title = title
        self.author = author
    def get_title(self) -> str: #the title is given and it is expected to be string
        return self.title
    def get_author(self) -> str: #the name of the author is given expected to be string
        return self.author
    def set_title(self, title: str): #set the title
        self.title = title
    def set_author(self, author: str): #set the author
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}") #the info for publication class such as title and author are displayed
        print(f"Author: {self.author}")

#class book is created and inherits things from class publication
class Book(Publication):
    def __init__(self, title, author, number_pages): #self, title, author and number of pages are initialized
        super().__init__(title, author) #I used super() to access a parent class from its child class
        self.number_of_pages = number_pages 
    def get_number_of_pages(self): #number of pages is given
        return self.number_of_pages
    def set_number_of_pages(self, number_pages): #set the number of pages
        if isinstance(number_pages, int) and number_pages > 0: #constraint: number of pages cannot be less than 0 :(
            self.number_of_pages = number_pages
        else:
            print("Number of pages must not be negative. Try again, it must not be negative this time.") #reply to wrong input

#class magazine is created and inherits stuff from its parent class publication
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author) #title and author inherited from parent class
        self.issue_number = issue_number #issue_number is defined
    def get_issue_number(self):
        return self.issue_number #get issue number
    def set_issue_number(self, issue_number): 
        self.issue_number = int(issue_number) #set issue number integer

#Main
if __name__ == "__main__":
    pub1 = Publication("Charles Scribner's Sons", "Ratchiff, R. & Van Dongen, H.") #created variables pub1, book1, mag for the source info
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
    mag = Magazine("National Geographic", "Various Authors", 202)
    print("Publication Information:") 
    pub1.display_info()
    print()
    print("Information for book:")
    book1.set_number_of_pages(-310)
    book1.display_info()
    print(f"Number of pages: {book1.get_number_of_pages()}")
    print()
    print("Information for magazine:")
    mag.display_info
    print(f"Issue number: {mag.get_issue_number()}")
