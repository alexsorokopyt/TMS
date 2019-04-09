# Написать функцию по решению квадратных уравнений.

from typing import Union


def quadratic_equation(coeff_a: Union[int, float], coeff_b: Union[int, float], coeff_c: Union[int, float]) -> Union[float, str]:
    """
    This function solves quadratic equation.

    Parameters
    ----------
    coeff_a: int, float
        Coefficient A of the given quadratic equation.
    coeff_b: int, float
        Coefficient B of the given quadratic equation.
    coeff_c: int, float
        Coefficient C of the given quadratic equation.

    Returns
    -------
    float
        Float roots of the quadratic equation, if discriminant is not equal to 0.
    str
        If discriminant is equal to 0.
    """
    discriminant = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if discriminant < 0:
        return 'Дискриминант меньше 0, уравнение не имеет корней'
    elif discriminant == 0:
        x = - coeff_b / (2 * coeff_a)
        return f'x = {x}'
    elif discriminant > 0:
        x1 = round((- coeff_b - discriminant ** 0.5) / (2 * coeff_a), 2)
        x2 = round((- coeff_b + discriminant ** 0.5) / (2 * coeff_a), 2)
        return f'x1 = {x1}, x2 = {x2}'


print(quadratic_equation(-1, -2, 1))