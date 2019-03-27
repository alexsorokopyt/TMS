# Дана целочисленная матрица размера 5х5. Получить новую матрицу
# путем деления всех элементов данной матрицы на ее наибольший по
# модулю элемент.

# Исходная матрица
matrix = [[1, 3, 6, 8, 9],
          [-15, 10, -24, 1, 1],
          [14, 3, 1, 4, 1],
          [5, 5, 12, 43, 21],
          [-1, -5, 0, 44, 1]
          ]

# Находим наибольший по модулю элемент
max_element = 0
for row in range(5):
    for column in range(5):
        if abs(matrix[row][column]) > max_element:
            max_element = abs(matrix[row][column])
print(f'Наибольшим по модулю числом является {max_element}\n')

# Заполняем новую матрицу
divided_matrix = []
for row in range(5):
    rows = []
    for column in range(5):
        rows.append(str(round(matrix[row][column] / max_element,4)))
    divided_matrix.append(rows)

# Делаем красивый вывод матрицы на экран
for row in range(5):
    rows = ' '.join(divided_matrix[row])
    print(rows)