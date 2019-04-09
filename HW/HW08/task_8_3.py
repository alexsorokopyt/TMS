# Возвращает сумму квадратного корня из числа и самого числа, деленную на 2.

from typing import Union

def fraction(number: Union[int, float]) -> float:
    """
    This function returns sum of square root of number and number itself divided by 2.

    Parameters
    ----------
    number: int, float
        Given number that will be processed.

    Returns
    -------
    float
        Sum of square root of number and number itself divided by 2.
    """
    return round((number ** 0.5 + number) / 2, 2)

result = fraction(5) + fraction(12) + fraction(19)
print(result)