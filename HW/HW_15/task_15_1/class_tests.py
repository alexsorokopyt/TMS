from class_mytime import MyTime
from unittest import TestCase


class MyTimeTests(TestCase):
    def setUp(self):
        self.time1 = MyTime(1, 1, 1)
        self.time2 = MyTime(1, 2, 3)
        self.time3 = MyTime(1, 1, 1)

    def test_is_equal(self):
        self.assertEqual(self.time1 == self.time2, False)

    def test_is_not_equal(self):
        self.assertEqual(self.time1 != self.time2, True)

    def test_is_less_than(self):
        self.assertEqual(self.time1 < self.time2, True)

    def test_is_greater_than(self):
        self.assertEqual(self.time1 > self.time2, False)

    def test_is_less_or_equal(self):
        self.assertEqual(self.time1 <= self.time3, True)

    def test_is_greater_or_equal(self):
        self.assertEqual(self.time1 >= self.time3, True)

    def test_add(self):
        self.assertEqual(self.time1 + self.time3, MyTime(2, 2, 2))

    def test_subtract(self):
        self.assertEqual(self.time1 - self.time2, MyTime(0, 0, 0))

    def test_multiply(self):
        self.assertEqual(self.time1 * 2, MyTime(2, 2, 2))

    def test_sting(self):
        self.assertEqual(self.time1, MyTime(1, 1, 1))
