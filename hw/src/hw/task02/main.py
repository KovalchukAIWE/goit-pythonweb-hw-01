import logging
from abc import ABC, abstractmethod
from typing import List

logging.basicConfig(level=logging.INFO)


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                break

    def get_all_books(self) -> List[Book]:
        return self._books.copy()


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book: Book = Book(title, author, year)
        self.library.add_book(book)
        logging.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logging.info(f"Book removed with title: {title}")

    def show_books(self) -> None:
        books: List[Book] = self.library.get_all_books()
        if not books:
            logging.info("Library is empty.")
        else:
            for book in books:
                logging.info(book)


def main() -> None:
    library: LibraryInterface = Library()
    manager: LibraryManager = LibraryManager(library)

    while True:
        command: str = input("Enter command (add, remove, show, exit): ").strip().lower()
        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
