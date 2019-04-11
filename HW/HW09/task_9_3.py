# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.

import functools


def remove_even_decorator(func):
    @functools.wraps(func)
    def wrapper(*args):
        remove_even = [number for number in args if number % 2]
        return remove_even
    return wrapper


@remove_even_decorator
def print_func(*args):
    print(args)


print(print_func(12, 15, 16, 17, 20))