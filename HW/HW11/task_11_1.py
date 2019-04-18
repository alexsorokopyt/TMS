# Создать класс Car. Атрибуты: марка, модель, год  выпуска,
# скорость(по умолчанию 0). Методы: увеличить скорости
# (скорость + 5), уменьшение скорости(скорость  - 5),
# стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_up(self, speed=5):
        self.__speed += speed

    def speed_down(self, speed=-5):
        self.__speed -= speed

    def reset_speed(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def reverse_speed(self):
        self.__speed *= -1