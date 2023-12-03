from copy import deepcopy
import unittest
from unittest.mock import Mock

'''
Задание 2.
У вас есть класс BookService, который использует интерфейс BookRepository
для получения информации о книгах из базы данных.
Ваша задача написать unit-тесты для BookService, используя Mockito для создания мок-объекта BookRepository.
'''


class Book:
    def __init__(self, book_id: str, title: str = None, author: str = None):
        self.book_id = book_id
        self.title = title
        self.author = author

    # Добавим метод для сравнения объектов по атрибутам
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self.book_id == other.book_id
            and self.title == other.title
            and self.author == other.author
        )

    def get_id(self):
        return self.book_id

    def set_id(self, book_id: str):
        self.book_id = book_id

    def get_title(self):
        return self.title

    def set_title(self, title: str):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author: str):
        self.author = author


class BookRepository:
    def __init__(self):
        self._books = []

    def find_by_id(self, book_id: str) -> Book | None:
        for book in self._books:
            if book.id == book_id:
                return book

    def find_all(self) -> list[Book]:
        return deepcopy(self._books)


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    @property
    def book_repository(self):
        return self._book_repository

    def find_book_by_id(self, book_id: str) -> Book:
        return self._book_repository.find_by_id(book_id)

    def find_all_books(self) -> list[Book]:
        return self._book_repository.find_all()


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_repository = Mock()
        self.book_service = BookService(book_repository=self.mock_repository)

    def test_find_book_by_id(self):
        expected_book = Book(book_id="123", title="Война и мир", author="Лев Толстой")
        self.mock_repository.find_by_id.return_value = expected_book

        result = self.book_service.find_book_by_id(book_id="123")

        self.mock_repository.find_by_id.assert_called_once_with("123")
        self.assertEqual(result, expected_book)

    def test_find_all_books(self):
        expected_books = [
            Book(book_id="1", title="Война и мир", author="Лев Толстой"),
            Book(book_id="2", title="Мертвые души", author="Николай Гоголь"),
        ]
        self.mock_repository.find_all.return_value = deepcopy(expected_books)

        result = self.book_service.find_all_books()

        self.mock_repository.find_all.assert_called_once()
        self.assertEqual(result, expected_books)


if __name__ == "__main__":
    unittest.main()
