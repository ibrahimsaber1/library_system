### Harry works in the library, Harry is tired of writing data in paper records so Harry decides to go digital.
### Harry wants a program to do all the operations in the library.
### Let's help Harry!

# Task 1 : 
#### task 1.1 Make Class(Library) with attributes:
    # booksList  
    # name of lirary  
    # lended books (name of user, book) 
#### task 1.2 Make method to display available Books.
#### task 1.3 Make method for books lending.
    # Don't forget to check if book isn't already lended 
#### task 1.4 Make method to add Book to library.
#### task 1.5 Make method to return borrowed book.
class Library:
    
    ## Attributes
    
    def __init__(self, lirary_name, booksList):
        self.lirary_name = lirary_name
        self.booksList = booksList
        self.lended_books = {} #{book_name:user_name}
        
    ## methodes
    
    def available_books(self):
        print("Available Books:")
        for book in self.booksList:
            print("-", book)

    def lend_book(self, user_name, book_name):
        if book_name in self.booksList:
            self.booksList.remove(book_name)
            self.lended_books[book_name] = user_name
            print(f"{book_name} has been successfully lent to {user_name}.")
        else:
            print("Sorry, this book is either not available or already lended.")

    def add_book(self, book_name):
        if book_name not in self.booksList:
            self.booksList.append(book_name)
            print(f"{book_name} has been added to the library.")
        else:
            print(f"{book_name} alrady on the library.")

    def return_book(self, book_name):
        if book_name in self.lended_books:
            del self.lended_books[book_name]
            self.booksList.append(book_name)
            print(f"{book_name} has been returned successfully.")
        else:
            print("This book was not borrowed from this library.")



# Example usage:
l1 = Library("Harry's Library", ["Book1", "Book2", "Book3"])


l1.available_books()

l1.lend_book("John", "Book2")

l1.available_books()

l1.add_book("Book4")

l1.available_books()

l1.return_book("Book2")

l1.available_books()
l1.available_books()
# Task 2 : 
#### task 2.1 Make object(Harry) with attributes:
    # booksList  = ['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS']
    # name of lirary  = "CodeWithHarry"
#### task 2.2 Make program run with this choices. __(Don't forget the welcome message)__
    # 1. Display Books
    # 2. Lend a Book
    # 3. Add a Book
    # 4. Return a Book
#### task 2.3 Make prgram ends or continue.
def harry():
    harrys_library = Library("CodeWithHarry", ['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'])
    print("Welcome to", harrys_library.lirary_name)

    while True:
        print("\nChoose an option:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
#         print("5. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            harrys_library.available_books()
        elif choice == '2':
            user_name = input("Enter your name: ")
            book_name = input("Enter the name of the book you want to lend: ")
            harrys_library.lend_book(user_name, book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book you want to add: ")
            harrys_library.add_book(book_name)
        elif choice == '4':
            book_name = input("Enter the name of the book you want to return: ")
            harrys_library.return_book(book_name)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        skip = input("do u want to continue (y/n)").lower()
        if skip == "n":
            print("Thank you for using", harrys_library.lirary_name)
            break


harry()
