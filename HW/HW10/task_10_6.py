# Дан файл, содержащий различные даты.
# Каждая дата - это число, месяц и год.
# Найти самую раннюю дату.

from datetime import datetime


def min_date_txt(file):
    with open(file) as file:
        dates = []
        for line in file.readlines():
            date = datetime.strptime(line.strip(), "%d.%m.%Y")
            dates.append(date)
        min_date = min(dates)
        return f'The earliest date in the given txt file is {min_date}'


print(min_date_txt('task_10_6.txt'))