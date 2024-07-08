from book_functions import load_book_from_json, print_books, add_book, remove_book
from book_functions import Book

if __name__ == "__main__":

    books = load_book_from_json('books.json')


    print("Seznam knih:")
    print_books(books)


    new_book = Book("New Book", "New Author", 2023, "978-1234567890")
    add_book('books.json', new_book)
    print("\nPo přidání nové knihy:")
    books_after_addition = load_book_from_json('books.json')
    print_books(books_after_addition)


    isbn_to_remove = "978-1234567890"
    remove_book('books.json', isbn_to_remove)
    print("\nPo odstranění knihy podle ISBN:")
    books_after_removal = load_book_from_json('books.json')
    print_books(books_after_removal)
