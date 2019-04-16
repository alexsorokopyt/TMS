# Имеется текстовый файл. Все четные строки этого файла записать во второй файл,
# а нечетные — в третий файл. Порядок следования строк сохраняется.


def odd_even_lines(file_1, file_2, file_3):
    with open(file_1) as file_1:
        even_lines = []
        odd_lines = []
        for index, line in enumerate(file_1.readlines()):
            if index % 2:
                even_lines.append(line)
            else:
                odd_lines.append(line)
    with open(file_2, 'w') as file_2:
        for line in even_lines:
            file_2.write(line)
    with open(file_3, 'w') as file_3:
        for line in odd_lines:
            file_3.write(line)


def main():
    odd_even_lines('task_10_3.txt', 'task_10_3_even.txt', 'task_10_3_odd.txt')


if __name__ == '__main__':
    main()

