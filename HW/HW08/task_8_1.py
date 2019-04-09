# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

from typing import Union


def different_means(mean_type: str, *args: Union[int, float]) -> Union[float, str]:
    """
    Returns requested type of mean - arithmetical or geometric.

    Parameters
    ----------
    mean_type: str
        Expected values are 'арифметическое' or 'геометрическое'
    args: int, float
        Given numbers

    Returns
    -------
    float, str
        Returns float if everything is OK.
        Returns str in case of error.
    """
    list_of_types = ['арифметическое', 'геометрическое']
    if mean_type in list_of_types:
        if mean_type.lower() == 'арифметическое':
            result = arithmetical_mean(*args)
        elif mean_type.lower() == 'геометрическое':
            result = geometric_mean(*args)
        return result
    else:
        return 'Ошибка. Запрашиваемая операция не найдена.'


def arithmetical_mean(*args: Union[int, float]) -> float:
    """
    Calculates arithmetical mean of given arguments.

    Parameters
    ----------
    args: int, float
        Given numbers

    Returns
    -------
    float
        Returns float of arithmetical mean.
    """
    length = len(args)
    sum_of_args = 0
    for arg in range(length):
        sum_of_args += args[arg]
    return round(sum_of_args / length, 3)


def geometric_mean(*args: Union[int, float]) -> Union[float,str]:
    """
    Calculates geometric mean of given arguments.

    Parameters
    ----------
    args: int, float
        Given numbers

    Returns
    -------
    float, str
        Returns float of geometric mean.
        If there is an error, returns str.
    """
    length = len(args)
    product_of_args = 1
    for arg in range(length):
        product_of_args *= args[arg]
    if product_of_args < 0:
        if not length % 2:
            return 'Ошибка. Корней четной степени из отрицательных чисел не существует.'
        else:
            return round(-((- product_of_args)  (1/length)), 3)
    else:
        return round(product_of_args  (1/length), 3)


print(different_means('арифметическое', 1,2,-3))
print(different_means('арифметическое', 1,2,3))
print(different_means('геометрическое', 1,2,-3, 3))
print(different_means('геометрическое', 1,2,-3))
print(different_means('геометрическое', 1,2,3))