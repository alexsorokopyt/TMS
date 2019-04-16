# В конец существующего текстового файла записать три новые строки текста. Записываемые строки вводятся с клавиатуры.


def add_3_lines(file):
    with open(file, 'a') as my_file:
        for new_line in range(3):
            new_line = input('Enter your text --> ')
            my_file.write(f'\n{new_line}')


def main():
    add_3_lines('task_10_1.txt')


if __name__ == '__main__':
    main()