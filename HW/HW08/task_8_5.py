# Описать функцию is_power_n(k, n) логического типа, возвращающую True,
# если целый параметр k (> 0) является степенью числа n (> 1),
# и False в противном случае.
# Дано число n (> 1) и набор из 10 целых положительных чисел.
# С помощью функции is_power_n найти количество степеней числа N в данном наборе.

from math import log


def is_power_n(number_in_power: int, number: int) -> bool:
    """
    Function checks whether the first parameter is the power of the second parameter.

    Parameters:
    -----------
    number_in_power: int
        Given parameter, which is supposed to be the power of the second parameter.
    number: int
        Given parameter, which is supposed to be the base.

    Returns:
    --------
    bool
        Returns boolean value. True if the the first parameter is the power of the second parameter
        and False if the opposite.
    """
    if number_in_power > 0 and number > 1:
        if not log(number_in_power, number) % 1:
            return True
        else:
            return False


number = 5
array = [0.25, 125, 5, 13, 14, 125]
counter = 0
for element in array:
    if is_power_n(element, number):
        counter += 1
print(counter)