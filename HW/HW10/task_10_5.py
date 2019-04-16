# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл.

import json
from random import randint


def matrix_to_json(file):
    with open(file, 'w') as my_file:
        random_matrix = [[randint(0, 9) for j in range(5)] for i in range(5)]
        json_matrix = json.dumps({'matrix': random_matrix})
        my_file.write(json_matrix)


def modify_json(file_1, file_2):
    with open(file_1) as file_1, open(file_2, 'w') as file_2:
        matrix = json.loads(file_1.read())
        for row in matrix['matrix']:
            for index in range(len(row)):
                if not row[index] % 2:
                    row[index] = 0
        json_matrix = json.dumps({'matrix_without_even_elements': matrix['matrix']})
        file_2.write(json_matrix)


def main():
    matrix_to_json('task_10_5_1.json')
    modify_json('task_10_5_1.json', 'task_10_5_2.json')


if __name__ == '__main__':
    main()