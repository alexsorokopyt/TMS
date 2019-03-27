# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.

while True:
    m = input('Введите m: ')
    n = input('Введите n: ')
    if m.isdigit() == False or n.isdigit() == False:
        print('Введенные данные должны быть числами\n')
        continue
    elif m > n:
        print('m должно быть меньше n!\n')
        continue
    else:
        m = int(m)
        n = int(n)
        break

for number in range(m, n + 1):
    factors = []
    for factor in range(2,number):
        if not number % factor:
            factors.append(factor)
    factors = ', '.join(str(factor) for factor in factors)
    print(f'{number}: {factors}')