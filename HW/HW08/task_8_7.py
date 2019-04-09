# Описать функцию fact2( n ) вещественного типа, вычисляющую двойной факториал:
# n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное
# (n > 0 — параметр целого типа. С помощью этой функции найти двойные факториалы
# пяти данных целых чисел

def fact2(n: int) -> str:
    """
    This function calculates double factorial of a number.

    Parameters
    ----------
    n: int
        Given number that will be processed.

    Returns
    -------
    str
        Double factorial of the number with word explanation.
    """
    product_of_n = 1
    if isinstance(n, int):
        if n >= 0:
            if not n % 2:
                for number in range(2, n + 1, 2):
                    product_of_n *= number
            elif n % 2:
                for number in range(1, n + 1, 2):
                    product_of_n *= number
            return f'Двойной факториал {n} равен {product_of_n}'
        else:
            return 'Входное число должно быть неотрицательным'
    else:
        return 'Тип данных не поддерживается'