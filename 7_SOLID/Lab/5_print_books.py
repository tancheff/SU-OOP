from abc import abstractmethod, ABC


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class PaperFormatter(BaseFormatter):
    def format(selfself, book: Book) -> str:
        return f"{book.title}\n{book.author}\n{book.content[:4]}"


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = format

    def get_book(selfself, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book
