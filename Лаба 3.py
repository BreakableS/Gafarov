class Book:
    """ Базовый класс книги. """
    def init(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def str(self):
        return f"Книга {self.name}. Автор {self.author}"

    def repr(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().init(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self):
        return f"{super().str()} Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().init(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"{super().str()} Продолжительность: {self.duration} ч"

paper_book = PaperBook("Маугли", "Редьярд Джозеф Киплинг", 896)
print(paper_book)

audio_book = AudioBook("Муму", "Иван Тургенев", 2.1)
print(audio_book)