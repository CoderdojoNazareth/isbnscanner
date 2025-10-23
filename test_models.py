import pytest
from models import Book


def test_book_creation():
    book = Book(
        isbn="1234567890",
        auteur="Test Author",
        titel="Test Title",
        plaats="Test Location",
    )
    assert book.isbn == "1234567890"
    assert book.auteur == "Test Author"
    assert book.titel == "Test Title"
    assert book.plaats == "Test Location"


def test_book_creation_with_kwargs():
    book = Book(
        isbn="1234567890",
        auteur="Test Author",
        titel="Test Title",
        plaats="Test Location",
        extra_field="Extra Value",
        AnotherField="Another Value",
    )
    assert book.extra_field == "Extra Value"
    assert book.anotherfield == "Another Value"


def test_book_repr():
    book = Book(
        isbn="1234567890",
        auteur="Test Author",
        titel="Test Title",
        plaats="Test Location",
    )
    expected_repr = "<Book ISBN: 1234567890, Auteur: Test Author, Title: Test Title, Plaats: Test Location>"
    assert repr(book) == expected_repr
