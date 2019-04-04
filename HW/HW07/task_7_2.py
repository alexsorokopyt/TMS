# Написать программу, со следующим интерфейсом: пользователю предоставляется
# на выбор 12 вариантов перевода(описанных в первой задаче). Пользователь
# вводит цифру от одного до двенадцати. После программа запрашивает ввести
# численное значение. Затем программа выдает конвертированный результат.
# Использовать функции из первого задания. Программа должна быть в
# бесконечном цикле. Код выхода из программы - “0”.

import task_7_1 as converter

print('\nВы можете выбрать 1 из 12 вариантов перевода:\n1. Дюймы в сантиметры\n2. Сантиметры в дюймы'
          '\n3. Мили в километры\n4. Километры в мили\n5. Фунты в килограммы\n6. Килограммы в фунты'
          '\n7. Унции в граммы\n8. Граммы в унции\n9. Галлон в литры\n10. Литры в галлоны'
          '\n11. Пинты в литры\n12. Литры в пинты\n\nДля выхода из программы введите 0')

while True:
    variant = input('\nВыберите желаемый вариант перевода: ')
    if variant == '0':
        break
    elif variant.isdigit():
        variant = int(variant)
        if variant > 12:
            print('Такого варианта нет!')
            continue
    elif not variant.isdigit():
        print('Номер варианта должен быть числом!')
        continue

    variant_unit = (
        ('дюймов', 'сантиметрах'),
        ('сантиметров', 'дюймах'),
        ('миль', 'километрах'),
        ('километров', 'милях'),
        ('фунтов', 'килограммах'),
        ('килограмм', 'фунтах'),
        ('унций', 'граммах'),
        ('грамм', 'унциях'),
        ('галлонов', 'литрах'),
        ('литров', 'галлонах'),
        ('пинт', 'литрах'),
        ('литров', 'пинтах')
    )

    unit = variant_unit[variant - 1][0]

    value = input(f'Введите количество {unit}: ')
    if value.isdigit():
        value = int(value)
    else:
        print('Значение должно быть числом!')

    if variant == 1:
        result = converter.InchToCentimetr(value)
    elif variant == 2:
        result = converter.CentimetrToInch(value)
    elif variant == 3:
        result = converter.MileToKilometer(value)
    elif variant == 4:
        result = converter.KilometerToMile(value)
    elif variant == 5:
        result = converter.PoundToKilogram(value)
    elif variant == 6:
        result = converter.KilogramToPound(value)
    elif variant == 7:
        result = converter.OunceToGram(value)
    elif variant == 8:
        result = converter.GramToOunce(value)
    elif variant == 9:
        result = converter.GallonToLiter(value)
    elif variant == 10:
        result = converter.LiterToGallon(value)
    elif variant == 11:
        result = converter.PintToLiter(value)
    elif variant == 12:
        result = converter.LiterToPint(value)

    resul_unit = variant_unit[variant - 1][1]
    print(f'Конвертированное значение в {resul_unit}: {result}')