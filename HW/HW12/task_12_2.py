# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения, сложения,
# вычитания, умножения на число, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида:
# одна строка, три числа, другой объект класса MyTime,
# и отсутствие входных параметров.


class MyTime():
    def __init__(self, *args):
        for arg in args:
            if type(arg) == int:
                self.hours = args[0]
                self.minutes = args[1]
                self.seconds = args[2]
            elif type(arg) == str:
                args_split = arg.split(':')
                self.hours = int(args_split[0])
                self.minutes = int(args_split[1])
                self.seconds = int(args_split[2])
            elif type(arg) == MyTime:
                self.hours = arg.hours
                self.minutes = arg.minutes
                self.seconds = arg.seconds
        if len(args) == 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.hours != other.hours or self.minutes != other.minutes or self.seconds != other.seconds:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.hours < other.hours or self.minutes < other.minutes or self.seconds < other.seconds:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.hours > other.hours or self.minutes > other.minutes or self.seconds > other.seconds:
            return True
        else:
            return False

    def __le__(self, other):
        if self.hours <= other.hours or self.minutes <= other.minutes or self.seconds <= other.seconds:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.hours >= other.hours or self.minutes >= other.minutes or self.seconds >= other.seconds:
            return True
        else:
            return False

    def __add__(self, other):
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds
        if seconds > 59:
            minutes += 1
            seconds %= 60
        if minutes > 59:
            hours += 1
            minutes %= 60
        return MyTime(hours, minutes, seconds)

    def __sub__(self, other):
        hours = self.hours - other.hours
        minutes = self.minutes - other.minutes
        seconds = self.seconds - other.seconds
        if seconds < 0:
            minutes -= 1
            seconds %= 60
        if minutes < 59:
            hours -= 1
            minutes %= 60
        return MyTime(hours, minutes, seconds)

    def __mul__(self, number):
        hours = self.hours * number
        minutes = self.minutes * number
        seconds = self.seconds * number
        if seconds > 59:
            minutes += seconds // 60
            seconds %= 60
        if minutes > 59:
            hours += minutes // 60
            minutes %= 60
        return MyTime(hours, minutes, seconds)

    def __repr__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'