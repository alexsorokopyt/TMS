# Создать статичный метод get_random_name в классе Pet. Метод возвращает случайную строку вида A-42.

from random import (randint,
                    choice,
                    )
from string import ascii_letters


class Pet:
    @staticmethod
    def get_random_name():
        return f'{choice(ascii_letters).upper()}-{randint(10, 99)}'

    @staticmethod
    def get_random_name_1():
        upper_eng_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        return f'{upper_eng_letters[randint(0, len(upper_eng_letters) - 1)]}-{randint(10, 99)}'


print(Pet.get_random_name())
print(Pet.get_random_name_1())