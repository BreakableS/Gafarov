if __name__ == "__main__":
    class Book:
        """Базовый класс для книг."""

        def init(self, title: str, author: str, genre: str):
            """Инициализация книги с указанием заглавия, автора и жанра."""
            self._title = title
            self._author = author
            self._genre = genre

        def get_title(self) -> str:
            """Получить заглавие книги."""
            return self._title

        def get_author(self) -> str:
            """Получить автора книги."""
            return self._author

        def get_genre(self) -> str:
            """Получить жанр книги."""
            return self._genre

        def str(self) -> str:
            """Строковое представление книги."""
            return f"{self._title} by {self._author} ({self._genre})"

        def repr(self) -> str:
            """Представление книги."""
            return f"{self.__class__.__name__}(title='{self._title}', author='{self._author}', genre = '{self._genre}')"


    class Novel(Book):
        """Дочерний класс для романов."""

        def init(self, title: str, author: str, genre: str, theme: str):
            """Инициализация романа с указанием заглавия, автора, жанра и темы."""
            super().init(title, author, genre)
            self._theme = theme

        def get_theme(self) -> str:
            """Получить тему романа."""
            return self._theme

        def str(self) -> str:
            """Строковое представление романа."""
            return f"{super().str()}, Theme: {self._theme}"


    class Detective(Book):
        """Дочерний класс для детективов."""

        def init(self, title: str, author: str, genre: str, detective_type: str):
            """Инициализация детектива с указанием заглавия, автора, жанра и типа детектива."""
            super().init(title, author, genre)
            self._detective_type = detective_type

        def get_detective_type(self) -> str:
            """Получить тип детектива."""
            return self._detective_type

        def str(self) -> str:
            """Строковое представление детектива."""
            return f"{super().str()}, Detective Type: {self._detective_type}"
    pass
