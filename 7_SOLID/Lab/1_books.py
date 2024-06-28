from typing import List


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.current_page = 0

    def turn_page(self, page):
        self.current_page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
        else:
            raise ValueError("Book already added.")

    def find_book(self, book_title: str):
        book = next(filter(lambda b: b.title == book_title, self.books), None)
        if book:
            return book
