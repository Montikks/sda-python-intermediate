import json
from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str

def load_book_from_json(file_name: str) -> List[Book]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        books = []
        for book_data in data.get('books', []):
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                year=int(book_data['year']),
                isbn=book_data['isbn']
            )
            books.append(book)
    return books


def print_books(books: List[Book]):
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book.title} by {book.author} ({book.year}), ISBN: {book.isbn}")
    print(f"\nPocet knih: {len(books)}")

def add_book(file_name: str, book: Book):
    with open(file_name, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        books = data.get('books', [])
        books.insert(0, {
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'isbn': book.isbn
        })
        data['books'] = books
        file.seek(0)
        json.dump(data, file, indent=4)

def remove_book(file_name: str, isbn: str):
    with open(file_name, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        books = data.get('books', [])
        filtered_books = [book for book in books if book['isbn'] != isbn]
        data['books'] = filtered_books
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
