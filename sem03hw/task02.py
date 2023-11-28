import unittest

# Задание 2.
# Разработайте и протестируйте метод numberInInterval, который проверяет,
# попадает ли переданное число в интервал (25;100).
# public boolean numberInInterval(int n) { ... }

MIN_NUM = 25
MAX_NUM = 100


def number_in_interval(n: int) -> bool:
    return MIN_NUM < n < MAX_NUM


class TestNumberInInterval(unittest.TestCase):
    def test_small_number(self):
        """Проверка слишком маленького числа"""
        self.assertFalse(number_in_interval(-123))

    def test_good_number(self):
        """Проверка подходящего числа"""
        self.assertTrue(number_in_interval(53))

    def test_big_number(self):
        """Проверка слишком большого числа"""
        self.assertFalse(number_in_interval(234))
