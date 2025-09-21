from models import Book
from typing import List, Optional

class BookService:
    def __init__(self, books: List[Book]):
        self._books = books

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        for book in self._books:
            book_isbn = book.isbn
            if book_isbn == isbn:
                return book

        return None

    def total_nr_of_books(self):
        len(self._books)
