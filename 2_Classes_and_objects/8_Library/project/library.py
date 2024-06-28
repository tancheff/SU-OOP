from typing import List
from user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []

        self.books_available: dict[str: List[str]] = {}
        # {authors: [books]}

        self.rented_books: dict[int: dict[str: int]] = {}
        # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        for available_author, available_books in self.books_available.items():
            if book_name in available_books:
                available_books.remove(book_name)
                self.rented_books[user.username] = {book_name: days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for users, books in self.rented_books.items():
            if book_name in books:
                return (f'The book "{book_name}" is already rented and will be available '
                        f'in {books[book_name]} days!')

    def return_book(self, author: str, book_name: str, user: User) -> None or str:
        if book_name in user.books:
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
