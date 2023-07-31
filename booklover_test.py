import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        t = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        new_book = "Old Man's War"
        t.add_book(new_book, 5)
        
        self.assertTrue(new_book in list(t.book_list['book_name']))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        t = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        new_book = "Old Man's War"
        t.add_book(new_book, 5)
        t.add_book(new_book, 3)
        
        self.assertEqual(t.book_list['book_name'].value_counts()[new_book], 1)

    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        t = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        new_book = "Old Man's War"
        t.add_book(new_book, 4)
        
        self.assertTrue(t.has_read(new_book))

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        t = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        new_book = "Old Man's War"
        t.add_book(new_book, 4)
        
        self.assertTrue(t.has_read(new_book))

    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        t = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t.add_book("Old Man's War", 4)
        t.add_book("The Old Man and the Sea", 5)
        t.add_book("Thrawn", 3)
        
        self.assertEqual(t.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        t = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t.add_book("Old Man's War", 4)
        t.add_book("The Old Man and the Sea", 2)
        t.add_book("Thrawn", 3)
        
        self.assertTrue(all(t.fav_books()['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)