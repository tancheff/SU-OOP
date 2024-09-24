from project.bookstore import Bookstore
from unittest import TestCase
import unittest


class TestBookstore(TestCase):
    def setUp(self):
        self.store = Bookstore(10)
        self.store.availability_in_store_by_book_titles = {
            "book_1": 1,
            "book_2": 2,
            "book_3": 3
        }

    def test_initialisation(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({"book_1": 1, "book_2": 2, "book_3": 3},
                         self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_books_limit_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.store.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))
        self.assertEqual(self.store.books_limit, 10)

    def test_books_limit_setter(self):
        self.store.books_limit = 5
        self.assertEqual(5, self.store.books_limit)

    def test_len(self):
        self.assertEqual(len(self.store), 6)

    def test_receive_book_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("book_4", 5)

        self.assertEqual("Books limit is reached. Cannot receive more books!",
                         str(ex.exception))

    def test_receive_book_existing(self):
        self.store.receive_book("book_3", 3)
        self.assertEqual(self.store.availability_in_store_by_book_titles["book_3"], 6)
        # self.assertEqual({"book_1": 1, "book_2": 2, "book_3": 6},
        #                  self.store.availability_in_store_by_book_titles)

    def test_receive_book_existing_return_statement(self):
        self.assertEqual(self.store.receive_book("book_3", 3),
                         "6 copies of book_3 are available in the bookstore.")

    def test_receive_book_zero_units(self):
        self.assertEqual(self.store.receive_book("book_4", 0),
                         "0 copies of book_4 are available in the bookstore.")
        self.assertEqual(self.store.availability_in_store_by_book_titles["book_4"], 0)

    def test_receive_book_new(self):
        self.store.receive_book("book_4", 3)
        self.assertEqual(self.store.availability_in_store_by_book_titles["book_4"], 3)
        # self.assertEqual({"book_1": 1, "book_2": 2, "book_3": 3, "book_4": 3},
        #                  self.store.availability_in_store_by_book_titles)

    def test_receive_book_new_return_statement(self):
        self.assertEqual(self.store.receive_book("book_4", 3),
                         "3 copies of book_4 are available in the bookstore.")

    def test_sell_book_unavailable(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("book_4", 4)

        self.assertEqual("Book book_4 doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_copies(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("book_3", 10)

        self.assertEqual("book_3 has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_successfully(self):
        self.store.sell_book("book_3", 2)
        self.assertEqual(self.store.availability_in_store_by_book_titles["book_3"], 1)
        self.assertEqual(self.store.total_sold_books, 2)

    def test_sell_book_successfully_return_statement(self):
        self.assertEqual(self.store.sell_book("book_3", 2),
                         "Sold 2 copies of book_3")

    def test_sell_book_with_no_copies_left(self):
        self.assertEqual(self.store.sell_book("book_3", 3),
                         "Sold 3 copies of book_3")

        self.assertEqual(self.store.availability_in_store_by_book_titles["book_3"], 0)

    def test_str_(self):
        self.assertEqual("Total sold books: 0\n"
                         "Current availability: 6\n"
                         " - book_1: 1 copies\n"
                         " - book_2: 2 copies\n"
                         " - book_3: 3 copies",
                         self.store.__str__())


if __name__ == '__main__':
    unittest.main()
