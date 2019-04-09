# Дан массив целых чисел A.
# Найти суммы положительных и отрицательных элементов массива, используя функцию определения суммы.

from typing import (
    List,
    Union
)

array = [1, 3, -5, 10, -12, -23]


def sum_depending_on_sign(array: List[Union[int, float]]) -> str:
    """
    This function returns sum of int and float elements depending on their sign.
    If there are any str elements in the array, the function returns error.

    Parameters
    ----------
    array : list[int, float]
        List of input elements.

    Returns
    -------
    str
        String with two sums and explanations to them.
    """
    sum_negative = 0
    sum_positive = 0
    for element in array:
        if isinstance(element, (int, float)):
            if element > 0:
                sum_positive += element
            else:
                sum_negative += element
        else:
            return 'Не все входные данные являются числами'
    return f'Сумма положительных чисел равна {sum_positive}.\nСумма отрицательных чисел равна {sum_negative}.'


print(sum_depending_on_sign(array))