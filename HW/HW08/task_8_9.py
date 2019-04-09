# Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε — вещественные, ε > 0),
# находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε .
# С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε .

# Не работает для больших X

from math import sin
from typing import Union

print(sin(12))


def sin1(x: Union[int, float], error: Union[int, float]) -> float:
    """
    Calculates the value of sin x with a given accuracy.

    Parameters:
    -----------
    x: int, float
        For what number sinus is to be calculated.
    error: int, float
        Tells how many decimal places to calculate accurately.

    Returns:
    --------
    float
        The float value of sin x.
    """
    sinus = 0
    n = 0
    while True:
        addend = (((-1) ** n) * (x ** (2 * n + 1))) / factorial(n)
        if abs(addend) > error:
            sinus += addend
        else:
            break
        n += 1
    return round(sinus, 3)


def factorial(n):
    product = 1
    for number in range(1, 2 * n + 2):
        product *= number
    return product


print(sin1(12, 0.1))