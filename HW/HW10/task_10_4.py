# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки. Если нет, то получить
# номер первой строки, в которой эти файлы отличаются друг от друга.


def compare_files(file_1, file_2):
    with open(file_1) as file_1, open(file_2) as file_2:
        file_1_lines = file_1.readlines()
        file_2_lines = file_2.readlines()
        for index in range(len(file_1_lines)):
            if file_1_lines[index] != file_2_lines[index]:
                print(f'Files differ on line {index + 1}')
                break

def main():
    compare_files('task_10_4_1.txt', 'task_10_4_2.txt')


if __name__ == '__main__':
    main()