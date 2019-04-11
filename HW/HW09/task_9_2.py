# Создать lambda функцию, которая принимает на вход неопределенное количество
# именных аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(a=5, sos=3, abc=5))