# Имеется текстовый файл. Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.


def copy_file(file_1, file_2):
    with open(file_1) as file_1:
        file_1_lines = []
        for line in file_1.readlines():
            if '0' in line:
                line = line.replace('0', '1')
            elif '1' in line:
                line = line.replace('1', '0')
            file_1_lines.append(line)
    with open(file_2, 'w') as file_2:
        for line in file_1_lines:
            file_2.write(line)


def main():
    copy_file('task_10_2_1.txt', 'task_10_2_2.txt')


if __name__ == '__main__':
    main()