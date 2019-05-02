from figure_classes import (
    Point,
    Circle,
    Triangle,
    Square,
)
from unittest import TestCase
from math import pi


class FiguresTests(TestCase):
    def setUp(self):
        self.square_point1 = Point(1, 1)
        self.square_point2 = Point(2, 2)
        self.triangle_point1 = Point(0, 0)
        self.triangle_point2 = Point(0, 1)
        self.triangle_point3 = Point(1, 0)
        self.square = Square(self.square_point1, self.square_point2)
        self.triangle = Triangle(self.triangle_point1, self.triangle_point2, self.triangle_point3)
        self.circle = Circle(self.triangle_point1, 1)

    def test_square_area(self):
        self.assertAlmostEqual(self.square.calc_area(), 1)

    def test_square_perimeter(self):
        self.assertEqual(self.square.calc_perimeter(), 4)

    def test_triangle_perimetr(self):
        self.assertAlmostEqual(self.triangle.calc_perimeter(), 3.41421356)

    def test_triangle_area(self):
        self.assertAlmostEqual(self.triangle.calc_area(), 0.5)

    def test_circle_area(self):
        self.assertAlmostEqual(self.circle.calc_area(), pi)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(self.circle.calc_perimeter(), 2 * pi)

    def test_point_x(self):
        self.assertEqual(self.square_point1.x, 1)

    def test_point_y(self):
        self.assertEqual(self.square_point1.y, 1)

    def test_figure_calc_dist(self):
        self.assertEqual(self.square.calc_dist(self.triangle_point1, self.triangle_point2), 1)
