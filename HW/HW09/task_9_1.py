# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.

list_of_words = ['Teach', 'Me', 'Skills', 'in', 'Python']
format_list = [f'{list_of_words.index(word)} - {word}' for word in list_of_words]
print(format_list)