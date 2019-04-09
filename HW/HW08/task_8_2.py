# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Подсказка: для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get()

from typing import Union


def count_number_of_times(*args: Union[int, float]) -> dict:
    """
    This function counts how many times each number is in the given list.

    Parameters:
    -----------
    args: int, float
        Any int or float number

    Returns:
    --------
    dict
        Returns a dictionary in the form of 'number' : 'how many time it was in the list'.
    """
    times_of_each_number = {}
    for arg in args:
        if times_of_each_number.get(arg) is None:
            times_of_each_number[arg] = 0
        for key, value in times_of_each_number.items():
            if arg == key:
                value += 1
            times_of_each_number[key] = value
    return times_of_each_number


print(count_number_of_times(1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 123, 345, 345, 321, 21, 21, 212, 212, 21, -21, -21))