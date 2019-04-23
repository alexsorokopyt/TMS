# Создать класс Point, описывающий точку(атрибуты x, y). Создать класс Figure.
# Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point),
# длина радиуса; методы: нахождение периметра и площади окружности),
# Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
# Square(атрибуты: две точки, методы: нахождение площади и периметра).
# При потребности создавать все необходимые методы не описанные в задании.

from math import pi


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle():
    def __init__(self, point: Point, radius):
        self.point_a = point
        self.radius = radius

    @property
    def perimeter(self):
        perimeter = 2 * pi * self.radius
        return perimeter

    @property
    def square(self):
        square = pi * (self.radius ** 2)
        return square


class Triangle():
    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    @property
    def side_a(self):
        side_a = ((self.point_a.x - self.point_b.x) ** 2 + (self.point_a.y - self.point_b.y) ** 2) ** 0.5
        return side_a

    @property
    def side_b(self):
        side_b = ((self.point_c.x - self.point_b.x) ** 2 + (self.point_c.y - self.point_b.y) ** 2) ** 0.5
        return side_b

    @property
    def side_c(self):
        side_c = ((self.point_a.x - self.point_c.x) ** 2 + (self.point_a.y - self.point_c.y) ** 2) ** 0.5
        return side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def square(self):
        half_perimeter = self.perimeter / 2
        square = (half_perimeter * (half_perimeter - self.side_a) * (half_perimeter - self.side_b) * (half_perimeter - self.side_c)) ** 0.5
        return square


class Square():
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    @property
    def length(self):
        length = abs(self.point_a.x - self.point_b.x)
        return length

    @property
    def width(self):
        width = abs(self.point_a.y - self.point_b.y)
        return width

    @property
    def square(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * self.length + 2 * self.width
