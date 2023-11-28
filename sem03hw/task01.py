import unittest
# Задание 1.
# Напишите тесты, покрывающие на 100% метод evenOddNumber,
# который проверяет, является ли переданное число четным или нечетным.
# (код приложен в презентации)
# public boolean evenOddNumber(int n) {
#     if (n % 2 == 0) {
#         return true;
#     } else {
#         return false;
#     }
# }


def even_odd_number(n: int) -> bool:
    return n % 2 == 0


class TestOddNumberMethod(unittest.TestCase):
    def test_odd_number(self):
        """Проверка чётного числа"""
        self.assertTrue(even_odd_number(2))

    def test_even_number(self):
        """Проверка нечётного числа"""
        self.assertFalse(even_odd_number(3))
