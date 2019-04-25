# Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# Добавить валидацию в конструкторе на ввод корректных данных. Создать иерархию ошибок.


class WrongStringError(Exception):
    def __init__(self, message='Неверное представление строки'):
        super().__init__(message)


class FirstLetterInLowercaseError(WrongStringError):
    def __init__(self, message='Первая буква должна быть заглавной'):
        super().__init__(message)


class NoSpaceError(WrongStringError):
    def __init__(self, message='Между словами нет пробела'):
        super().__init__(message)


class NotThatTypeError(Exception):
    def __init__(self, message='Содержит не тот тип данных'):
        super().__init__(message)


class NotIntError(NotThatTypeError):
    def __init__(self, message='Переменная должна быть числом'):
        super().__init__(message)


class NotStrError(NotThatTypeError):
    def __init__(self, message='Не является строкой'):
        super().__init__(message)


class TooMuchError(Exception):
    def __init__(self, message='Слишком большое значение'):
        super().__init__(message)


class TooLongStringError(TooMuchError):
    def __init__(self, message='Слишком длинное слово'):
        super().__init__(message)


class TooBigNumberError(TooMuchError):
    def __init__(self, message='Слишком большое число'):
        super().__init__(message)


class CurrencyError(Exception):
    def __init__(self, message='Не содержит единицы валюты'):
        super().__init__(message)


class Book:
    def __init__(self, pages, year, author, cost):
        if not isinstance(self.pages, int):
            raise NotIntError
        elif pages > 500:
            raise TooBigNumberError
        self.pages = pages

        if not isinstance(self.year, int):
            raise NotIntError
        elif pages > 2019:
            raise TooMuchError
        self.year = year

        if self.author[0] != self.author[0].upper():
            raise FirstLetterInLowercaseError
        elif not isinstance(self.author, str):
            raise NotStrError
        elif len(self.author) > 25:
            raise TooLongStringError
        elif len(self.author.split()) < 2:
            raise NoSpaceError
        self.author = author

        if not self.cost[0] == '$':
            raise CurrencyError
        self.cost = cost


def main():
    try:
        book = Book(178, 1997, 'Alexander Sokopyt', '$100')
    except FirstLetterInLowercaseError as err:
        print(err)
    except NoSpaceError as err:
        print(err)
    else:
        print('Усе чотка!')


if __name__ == '__main__':
    main()
