import json
from dataclasses import dataclass, asdict

# Task 1
# Napis funkciu load_book_from_json(file_name), ktora nacita knihy do dataclassy
# Book (ktoru treba tiez vytvorit)
# Format jsonu:
"""
{
    "books": [
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year": 1960,
            "isbn": "978-0061120084"
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "isbn": "978-0451524935"
        }
    ]
}
"""


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int
    isbn: str

    def __str__(self):
        return f'{self.title} by {self.author} from {self.year}. ISBN: {self.isbn}'


def load_book_from_json(file_name):
    loaded_books = []
    with open(file_name) as file:
        data = json.load(file)
        for book in data['books']:
            loaded_books.append(Book(**book))

    return loaded_books


# Task 2
# Napis funkciu print_books(books), ktora v peknom formate vypise vsetky knihy
# a na zaver vypise aj ich pocet

def print_books(books):
    for book in books:
        print(book)
    print(f'Book count: {len(books)}')

# Task 3
# Napis funkciu add_book(book, file_name), ktora upravi json file `books.json` tak, ze sa don
# prida nova kniha predana cez parameter `book` (typu `Book`)


def add_book(book, file_name):
    books = [*load_book_from_json(file_name), book]
    with open(file_name, 'w') as file:
        json.dump({'books': [asdict(book) for book in books]}, file, indent=4)

# Task 4
# Napis funkciu remove_book(isbn, file_name), ktora vymaze knihu z .json suboru podla isbn cisla.


def remove_book(isbn, file_name):
    new_books = [book for book in load_book_from_json(file_name) if book.isbn != isbn]
    with open(file_name, 'w') as file:
        json.dump({'books': [asdict(book) for book in new_books]}, file, indent=4)


if __name__ == "__main__":
    file_name = 'books.json'

    books = load_book_from_json(file_name)
    print_books(books)
    print()
    add_book(Book(title="Pride and Prejudice", author="Jane Austen", year=1813, isbn="978-1503290563"), file_name)
    books = load_book_from_json(file_name)
    print(books)
    print()
    remove_book("978-0061120084", file_name)
    remove_book("978-1503290563", file_name)
    print(books)
