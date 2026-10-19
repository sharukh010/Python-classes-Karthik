class Book: 
    # default constructor 
    # def __init__(self): 
    #     self.title = "Untitled"
    #     self.description = "No Description"
    #     self.pages = 0 
    #     self.content = "No content" 
    #     self.author = "unnamed"
    #     self.category = "uncategorized"
    # parameterized constructor 
    # def __init__(self,title,description,pages,content,author,category): 
    #     self.title = title 
    #     self.description = description
    #     self.pages = pages 
    #     self.content = content 
    #     self.author = author
    #     self.category = category
    # copy constructor 
    def __init__(self,book): 
        if book == None:
            self.title = "Untitled"
            self.description = "No Description"
            self.pages = 0 
            self.content = "No content" 
            self.author = "unnamed"
            self.category = "uncategorized" 
        else: 
            self.title = book.title 
            self.description = book.description 
            self.pages = book.pages 
            self.content = book.content 
            self.author = book.author 
            self.category = book.category 

    def display(self): 
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Pages: {self.pages}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author}")
        print(f"Category: {self.category}")

# creation of an object with copy constructor 
original_book = Book(None)
original_book.title = "Harry Potter"
original_book.description = "It's a harry potter book."
original_book.pages = 400 
original_book.content = "The story of harry potter"
original_book.author = "J.K Rowling"
original_book.category = "Fiction"

copy_book = Book(original_book)
copy_book.display()

# creation of object with parameterized constructor 
# book = Book(
#       "Harry Potter",
#       "This is a harry potter book",
#       400,
#       "This is the story of harry potter",
#       "J.K. Rowling",
#       "Fiction"
# )
# book.display()
# creation of object with default constructor 
# book = Book()
# book.display()
# book.title = "Harry Potter"
# book.description = "It's a harry potter book."
# book.pages = 400 
# book.content = "The story of harry potter"
# book.author = "J.K Rowling"
# book.category = "Fiction"
# print("#"*20)
# book.display()