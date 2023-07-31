import pandas as pd

class BookLover():
    """A person and their books and preferences"""
    
    def __init__(self, name, email, genre, num_books=0, book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.genre = genre
        self.num_books = num_books
        self.book_list = book_list
                
    def add_book(self, book, rating):
        if not (self.has_read(book)):
            new_book = pd.DataFrame({'book_name': [book], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print("Book already added")
        
    def has_read(self, book):
        if book in list(self.book_list['book_name']):
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    print(test_object.name, test_object.email, test_object.genre)
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Old Man's War", 4)
    test_object.add_book("Banana", 2)
    test_object.add_book("Thrawn", 3)
    test_object.add_book("Thrawn", 5)
    print(test_object.has_read("Thrawn"))
    print(test_object.num_books_read())
    print(test_object.book_list)
    print(test_object.fav_books())
    print(test_object.num_books_read())