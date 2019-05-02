# Создать класс Point, описывающий точку(атрибуты x, y).
# Создать класс Figure. Создать три дочерних класса
# Circle(атрибуты: координаты центра(тип Point), длина радиуса;
# методы: нахождение периметра и площади окружности),
# Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
# Square(атрибуты: две точки, методы: нахождение площади и периметра).
# При потребности создавать все необходимые методы не описанные в задании. [my-oop-03]

from math import pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    def calc_dist(self, point1, point2):
        dist = ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5
        return dist

    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def calc_area(self):
        return pi * self.radius ** 2

    def calc_perimeter(self):
        return 2 * pi * self.radius


class Triangle(Figure):
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def calc_area(self):
        area = 0.5 * abs((self.a.x - self.c.x) * (self.b.y - self.c.y) - (self.b.x - self.c.x) * (self.a.y - self.c.y))
        return area

    def calc_perimeter(self):
        dist1 = self.calc_dist(self.a, self.b)
        dist2 = self.calc_dist(self.b, self.c)
        dist3 = self.calc_dist(self.a, self.c)
        return dist1 + dist2 + dist3


class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_area(self):
        dist = self.calc_dist(self.a, self.b)
        area = dist ** 2 / 2
        return area

    def calc_perimeter(self):
        dist = self.calc_dist(self.a, self.b)
        perimeter = (dist / 2 ** 0.5) * 4
        return perimeter


c = Circle(Point(0, 0), 1)
print(c.calc_area())
print(c.calc_perimeter())

t = Triangle(Point(0, 3), Point(4, 0), Point(0, 0))
print(t.calc_area())
print(t.calc_perimeter())

s = Square(Point(0, 2), Point(2, 0))
print(s.calc_area())
print(s.calc_perimeter())