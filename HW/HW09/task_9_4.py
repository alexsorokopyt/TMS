# Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный.

import functools


def reverse_args_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args[::-1], **kwargs)
        return result
    return wrapper


@reverse_args_decorator
def print_arguments(*args, **kwargs):
    if args:
        print(args)
    if kwargs:
        print(kwargs)


print_arguments(1,2,3,4, a=5)