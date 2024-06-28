authors_books = {
    "George Orwell": ["1984", "Animal Farm"],
    "Harper Lee": ["To Kill a Mockingbird"],
    "F. Scott Fitzgerald": ["The Great Gatsby", "Tender Is the Night"],
    "Leo Tolstoy": ["War and Peace", "Anna Karenina"]
}

for authors, books in authors_books.items():
    print(f"{authors}: {books}")

my_book = "1984"
for authors, books in authors_books.items():
    if my_book in books:
        print(books)
